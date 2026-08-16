#!/usr/bin/env python3
"""Signed 2026-08-16 EF-4 realizable partial-staircase falsifier.
Deterministic; exact integer arithmetic; no seeds; direct F_n-compatible chains.
"""
from bisect import bisect_left, bisect_right
import json

RHOS=(3,4); CAP=1_000_000
EXPECTED=(40,40,0,0)  # requires, pass, failures, partial at (24,2)

def prescription(n,rho):
    h=n//2; p={1:1,h:h,h+1:h+1,n:n}
    for k in range(1,rho):
        p[h-rho+k]=n//4+k; p[h+1+k]=3*n//4+k
    assert len(p)==2*rho+2==len(set(p.values()))
    return p

def geom(n,rho):
    p=prescription(n,rho); pc=set(p.values()); h=n//2
    fr=tuple(r for r in range(1,n+1) if r not in p)
    fc=tuple(c for c in range(1,n+1) if c not in pc)
    pp=set(p.items())
    lo=tuple(sorted(x for x in pp if h-rho+1<=x[0]<=h-1))
    up=tuple(sorted(x for x in pp if h+2<=x[0]<=h+rho))
    pts=[]
    for r in range(1,n+1):
        pts.append((r,p[r])) if r in p else pts.extend((r,c) for c in fc)
    return p,pp,fr,fc,len(fr),lo,up,tuple(sorted(pts))

def inside(x,a,b): return a[0]<=x[0]<=b[0] and a[1]<=x[1]<=b[1]
def cnt(xs,a,b): return bisect_right(xs,b)-bisect_left(xs,a)

def partial(boxes,stairs):
    for a,b in boxes:
        for s in stairs:
            if s:
                k=sum(inside(x,a,b) for x in s)
                if 0<k<len(s): return True
    return False

def positive_control():
    s=((2,2),(3,3))
    return (partial((((1,1),(2,2)),),(s,)) and
            not partial((((4,4),(5,5)),),(s,)) and
            not partial((((1,1),(4,4)),),(s,)))

def chain_count(n,pts):
    vals=[1]*len(pts)
    for _ in range(3):
        bit=[0]*(n+2); nxt=[0]*len(pts); i=0
        while i<len(pts):
            j=i; r=pts[i][0]
            while j<len(pts) and pts[j][0]==r: j+=1
            for q in range(i,j):
                x=pts[q][1]-1; s=0
                while x: s+=bit[x]; x-=x&-x
                nxt[q]=s
            for q in range(i,j):
                x=pts[q][1]; v=vals[q]
                while x<len(bit): bit[x]+=v; x+=x&-x
            i=j
        vals=nxt
    return sum(vals)

def biting_adjacency(rho,fr,fc,N,pts):
    inc={x:[] for x in pts}; out={x:[] for x in pts}; rhs=N*(N+8*rho)
    for i,a in enumerate(pts):
        for b in pts[i+1:]:
            if a[0]<b[0] and a[1]<b[1]:
                ar=cnt(fr,a[0],b[0]); ac=cnt(fc,a[1],b[1])
                if 8*ar*ac>rhs:
                    out[a].append(b); inc[b].append(a)
    return inc,out

def verdict(n,rho,g,p1,p2,p3,p4):
    _,pp,fr,fc,N,lo,up,_=g; h=n//2
    pr=cnt(fr,p1[0],p2[0])*cnt(fc,p1[1],p2[1])
    fu=cnt(fr,p3[0],p4[0])*cnt(fc,p3[1],p4[1])
    small=8*min(pr,fu)<=N*(N+8*rho)
    fixed=p2==(h,h) and p3==(h+1,h+1)
    pc=any(inside(x,p1,p2) for x in up); fcross=any(inside(x,p3,p4) for x in lo)
    pl=not any(inside(x,p1,p2) for x in lo); fl=not any(inside(x,p3,p4) for x in up)
    pn=sum(inside(x,p1,p2) for x in pp); fn=sum(inside(x,p3,p4) for x in pp)
    loss=(not pc and not fcross and ((pl and pn<=3 and fn<=rho+2) or
                                     (fl and fn<=3 and pn<=rho+2)))
    part=partial(((p1,p2),(p3,p4)),(lo,up))
    return fixed,small,loss,part,{"past_prescribed":pn,"future_prescribed":fn,
      "past_crosses":pc,"future_crosses":fcross,"past_loses":pl,"future_loses":fl}

def run_pair(n,rho,limit):
    g=geom(n,rho); p,pp,fr,fc,N,lo,up,pts=g
    all4=chain_count(n,pts); inc,out=biting_adjacency(rho,fr,fc,N,pts)
    biting=part=req=passed=fail=0; first=None; witness=None
    for p2,aa in ((x,v) for x,v in inc.items() if v):
      for p3,dd in ((x,v) for x,v in out.items() if v):
       if p2[0]<p3[0] and p2[1]<p3[1]:
        for p1 in aa:
         for p4 in dd:
          biting+=1; req+=1
          fixed,small,loss,par,detail=verdict(n,rho,g,p1,p2,p3,p4)
          assert not small
          passed+=bool(fixed or loss)
          if par:
              part+=1
              if first is None: first={"points":[p1,p2,p3,p4],"detail":detail}
          if not (fixed or loss):
              fail+=1; witness={"points":[p1,p2,p3,p4],"prescription":sorted(pp),
                                "lower_stair":lo,"upper_stair":up,"detail":detail}
              return record(n,rho,N,all4,biting,part,req,passed,fail,False,False,first,witness)
          if biting>=limit:
              return record(n,rho,N,all4,biting,part,req,passed,fail,False,True,first,witness)
    return record(n,rho,N,all4,biting,part,req,passed,fail,True,False,first,witness)

def record(n,rho,N,all4,b,p,r,l,f,ex,cap,first,witness):
    return {"N":n,"RHO":rho,"FREE_COUNT":N,"COMPATIBLE_CHAINS":all4,
      "COMPATIBLE_BITING_CHAINS":b,"PARTIAL_STAIRCASE_CASES":p,
      "REQUIRES_LOSS_CASE":r,"LOSS_CASE_PASS":l,"COMPATIBLE_FAILURES":f,
      "PAIR_EXHAUSTED":ex,"CAP_HIT_IN_PAIR":cap,"FIRST_PARTIAL":first,"WITNESS":witness}

def show(x,cum):
    print("PAIR_BEGIN")
    for k in ("N","RHO","FREE_COUNT","COMPATIBLE_CHAINS","COMPATIBLE_BITING_CHAINS",
              "PARTIAL_STAIRCASE_CASES","REQUIRES_LOSS_CASE","LOSS_CASE_PASS",
              "COMPATIBLE_FAILURES","PAIR_EXHAUSTED","CAP_HIT_IN_PAIR"):
        print(f"{k}={x[k]}")
    print(f"CUMULATIVE_COMPATIBLE_BITING_CHAINS={cum}")
    if x["FIRST_PARTIAL"] is not None: print("FIRST_PARTIAL="+json.dumps(x["FIRST_PARTIAL"],sort_keys=True))
    if x["WITNESS"] is not None: print("WITNESS="+json.dumps(x["WITNESS"],sort_keys=True))
    print("PAIR_END")

def main():
    print("EF4_PARTIAL_STAIRCASE_SEARCH\nDETERMINISTIC=True\nRANDOM_SEEDS=NONE")
    print(f"COMPUTE_CAP_COMPATIBLE_BITING_CHAINS={CAP}\nCAP_EXCLUDES_CONTROLS=True\n")
    ok=positive_control()
    print(f"POSITIVE_CONTROL_PARTIAL_TRUE={ok}\nPOSITIVE_CONTROL_EMPTY_FALSE=True\nPOSITIVE_CONTROL_FULL_FALSE=True")
    if not ok: print("TERMINAL=POSITIVE_CONTROL_FAILED"); return 2
    print("POSITIVE_CONTROL=PASS\n")
    c=run_pair(24,2,CAP); observed=(c["REQUIRES_LOSS_CASE"],c["LOSS_CASE_PASS"],c["COMPATIBLE_FAILURES"],c["PARTIAL_STAIRCASE_CASES"])
    print("CONTROL_24_2_BEGIN")
    for k in ("REQUIRES_LOSS_CASE","LOSS_CASE_PASS","COMPATIBLE_FAILURES","PARTIAL_STAIRCASE_CASES"): print(f"{k}={c[k]}")
    print("CONTROL_24_2_END")
    if observed!=EXPECTED or not c["PAIR_EXHAUSTED"]: print("TERMINAL=CONTROL_REGRESSION_FAILED"); return 3
    print("CONTROL_REGRESSION=PASS\n")
    cum=0; n=34
    while True:
      for rho in RHOS:
       if n>=10*rho+4:
        x=run_pair(n,rho,CAP-cum); cum+=x["COMPATIBLE_BITING_CHAINS"]; show(x,cum)
        if x["COMPATIBLE_FAILURES"]: print("TERMINAL=REFUTED_BY_COMPATIBLE_WITNESS"); return 0
        if x["CAP_HIT_IN_PAIR"] or cum>=CAP: print("TERMINAL=OPEN_AT_COMPUTE_CAP"); return 0
        if x["PARTIAL_STAIRCASE_CASES"]:
            assert x["PAIR_EXHAUSTED"]
            print("TERMINAL=FIRST_PARTIAL_PAIR_EXHAUSTED_NO_FAILURE"); return 0
      n+=2

if __name__=="__main__": raise SystemExit(main())
