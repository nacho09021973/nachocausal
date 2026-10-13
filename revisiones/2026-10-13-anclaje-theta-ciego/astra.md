[DERIVACIÓN] La separación entre mínimos ordenados por radio puede ser menor que la distancia típica entre puntos del sembrado: la proyección radial reúne mínimos de toda la circunferencia. Por eso distingo la escala volumétrica, \(\rho^{-1/3}\), de la escala radial pertinente para la horquilla. Recomiendo esta última, con una normalización convencional explícita. La geometría permite deducir su exponente; no permite garantizar que la partición por \(O\) alcance esa resolución.

[DERIVACIÓN] Los mínimos se concentran cerca de la frontera inicial \(t^*=0\), que es espacial: su métrica inducida es
\[
h=(1+2M/r)\,dr^2+r^2d\phi^2.
\]
En dimensión espaciotemporal \(D\), el volumen del pasado de un punto situado a pequeña distancia temporal propia \(s\) de una frontera espacial crece como \(a_Ds^D\). La probabilidad de que ese pasado esté vacío es \(\exp(-\rho a_Ds^D)\). Integrar sobre \(s\) da una densidad superficial de mínimos proporcional a
\[
\rho\int_0^\infty e^{-\rho a_Ds^D}\,ds
\;\propto\;\rho^{(D-1)/D}.
\]
En consecuencia, en 2+1D aparecen aproximadamente \(\rho^{2/3}\) mínimos por unidad de superficie inicial. Al proyectarlos sobre \(r\), una franja recibe contribuciones de toda su extensión angular. La separación radial característica escala, por tanto, como
\[
\ell_{\mathrm{rad}}\propto
\frac{\rho^{-2/3}}{\text{longitud transversal}}.
\]
Este argumento es local y asintótico; los bordes y la curvatura introducen correcciones.

[SUPUESTO] Para convertirlo en un umbral congelado, adopto una **escala radial media de la caja**, no una estimación de la separación precisamente en la frontera inferida. Su longitud transversal será
\[
P_*=\frac{1}{r_{\max}-r_{\min}}
       \int_{r_{\min}}^{r_{\max}}2\pi r\,dr
    =\pi(r_{\max}+r_{\min})=1.4\pi.
\]
Equivale a evaluar el perímetro en \(r_*=0.7\). La elección usa exclusivamente los extremos de la caja y representa el volumen espacial coordenado disponible por unidad de radio. No presupone dónde está el horizonte ni depende de la partición, de semillas o del número realizado de puntos.

[DERIVACIÓN] Con esta elección, el traslado dimensional de la separación radial es
\[
\ell_{\mathrm{rad}}=\frac{\rho^{-2/3}}{P_*}.
\]
Sus unidades son de longitud: \(\rho^{-2/3}\) tiene unidades de área. En 1+1D no existe una dirección angular que se agregue. La medida transversal de dimensión cero es \(1\), y el mismo argumento produce \(\rho^{-(2-1)/2}=\rho^{-1/2}\). Con la normalización que explicito a continuación, la reducción a la fórmula sellada es exacta.

[SUPUESTO] Fijo el coeficiente de esta **escala de referencia** en uno, como en la regla sellada; no la identifico con la esperanza exacta de una separación entre vecinos. Esta distinción importa. En una aproximación plana, el coeficiente superficial exacto es
\[
c_D=\Gamma(1+1/D)a_D^{-1/D}.
\]
Así, \(c_2=\sqrt{\pi}/2\), mientras que
\(c_3=\Gamma(4/3)(3/\pi)^{1/3}\). La regla sellada tampoco incluye \(1/c_2\). Además, aquí la intensidad radial local contiene el factor métrico \(\sqrt{1+2M/r}\): aproximadamente,
\[
\lambda_r(r)=c_3\rho^{2/3}\,2\pi r\sqrt{1+2M/r}.
\]
Por tanto, mi fórmula no es \(1/\lambda_r(r)\). Los factores de orden uno que separan ambas cantidades quedan absorbidos convencionalmente en la tolerancia \(K_{\rm LOC}=2\), sin modificarla. Esto es una decisión de normalización, no una demostración de que dos unidades aseguren una cobertura determinada. La reducción exacta a 1+1D corresponde a esa convención compartida.

[SUPUESTO] Para que esta escala gobierne la horquilla, la partición debe aproximar una separación radial nítida: los mínimos relevantes de ambos grupos deben ser vecinos de una misma frontera. Si \(O\) mantiene una dispersión que mezcla radios alejados, la anchura estará dominada por clasificación, no por discretitud. Tampoco interpreto «no se puede localizar más fino» como una cota universal de inferencia: combinar muchos puntos puede producir estimadores con precisión superior a una separación típica.

[DERIVACIÓN] En el modelo ideal de una frontera fija y una intensidad radial local casi constante, las distancias al vecino de cada lado son aproximadamente exponenciales. Si su media es \(\delta\), la anchura tiene media \(2\delta\), y el punto medio tiene desviación típica \(\delta/\sqrt2\). Ambas magnitudes comparten escala, aunque sus constantes difieren. Esto justifica trasladar conjuntamente los dos umbrales sellados.

[SUPUESTO] Mantengo, por fidelidad a esa regla, \(\theta_{\rm stab}=2\ell_{\rm rad}\) y \(\theta_{\rm loc}=2\ell_{\rm rad}/(2M)\). El parámetro \(2M\) aparece en la fórmula final únicamente como unidad de puntuación. \(T=16\) no multiplica la densidad superficial inicial: prolongar la caja no genera proporcionalmente más mínimos. Sí afecta a los futuros y, por ello, a la clasificación.

[DERIVACIÓN] Los umbrales propuestos no son automáticamente decorativos por el soporte: son menores que la extensión radial \(1.2\), y los de estabilidad son menores que la máxima desviación poblacional posible, \(0.6\). Sin embargo, una frontera incorrecta pero reproducible puede satisfacer ambos; localización estrecha y estabilidad no demuestran exactitud.

[SUPUESTO] Hay riesgo de fallos persistentes si la clasificación conserva una anchura radial al aumentar \(\rho\), porque el umbral decrece como \(\rho^{-2/3}\). También hay riesgo de exigir demasiado mediante una regla «todas las semillas»: incluso idealmente, dos separaciones exponenciales suman menos de dos veces su media individual con probabilidad \(1-3e^{-2}\approx0.594\). \(K=2\) no define por sí solo un nivel de cobertura. Finalmente, la densidad radial varía con \(r\); usar su promedio puede resultar exigente cerca del borde interior. Estas limitaciones deben quedar registradas antes de observar resultados.

```text
FÓRMULA_FINAL
K_LOC = 2
P_* = π(1.3 + 0.1) = 1.4π
ell_rad(ρ) = ρ^(-2/3)/(1.4π)

theta_loc(ρ)  = [2/(0.5 · 1.4π)] ρ^(-2/3)
theta_stab(ρ) = [2/(1.4π)] ρ^(-2/3)

T = 16; ρ nominal congelada.
ρ       theta_loc       theta_stab
32      0.09023         0.04511
63      0.05744         0.02872
126     0.03619         0.01809
```