"""Exploratory Galerkin reconstruction; no spectral conclusions are certified."""
import json
from pathlib import Path

# Reuse the Galerkin assembly, exposing fixed-data reconstructions.
source = Path(__file__).with_name('explore_feedback.py').read_text()
source = source.split("if __name__")[0]
source = source.replace('def calc(N):', 'def calc(N):')
source = source.replace('F=[];D=[];T=[];BB=[]', 'F=[];D=[];T=[];BB=[];GG=[]')
source = source.replace('F.append(div);D.append(mixed);T.append', '''
  zi=da*ds[i]-(i*(i+1)+2)*ps[i]
  zj=da*ds[j]-(j*(j+1)+2)*ps[j]
  GG.append((zi[:,None]*zj[None,:]-zj[:,None]*zi[None,:])/np.sqrt(2))
  F.append(div);D.append(mixed);T.append''')
source = source.replace('return {\'N\':N,', '''
 gmat=np.array(GG).reshape(len(pairs),-1)*ww
 diagnostics=[]
 for n in range(5):
  cg=coeff[:,n]
  diagnostics.append({'degree':n,'g_norm':float(np.linalg.norm(cg@gmat)),
    'feedback_error':float(np.linalg.norm(feedback[:,n]-np.eye(N+2)[:,n])),
    'energy':float(cg@amat@cg)})
 return {'fixed_data':diagnostics,'N':N,''')
exec(compile(source, 'modified_galerkin', 'exec'))
if __name__ == '__main__':
    results = []
    for n in [8, 12, 18, 26, 36]:
        result = calc(n)
        print(json.dumps(result), flush=True)
        results.append(result)
    Path(__file__).with_name('fixed_boundary_exploration.json').write_text(
        json.dumps(results, indent=2) + '\n')
