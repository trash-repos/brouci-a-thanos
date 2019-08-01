using DelimitedFiles
using PyPlot            #pyplot()
using Plots; pgfplots()         # PGFPlots backend
using LaTeXStrings


cd("/home/strelda/Documents/mff/deterministický_chaos/brouci-a-thanos/data/")

d1 = readdlm("pocitej_output_10.0.txt", Float64)
d2 = readdlm("pocitej_output_30.0.txt", Float64)
d3 = readdlm("pocitej_output_50.0.txt", Float64)
d4 = readdlm("pocitej_output_70.0.txt", Float64)
d5 = readdlm("pocitej_output_90.0.txt", Float64)
d6 = readdlm("pocitej_output_110.0.txt", Float64)

mu_all = [d1[1:end,1];d2[1:end,1];d3[1:end,1];d4[1:end,1];d5[1:end,1];d6[1:end,1]]
L_all = [d1[1:end,2];d2[1:end,2];d3[1:end,2];d4[1:end,2];d5[1:end,2];d6[1:end,2]]
P_all = data[1:end,3]
A_all = data[1:end,4]

#=
model(x, p) = p[1]*sin.(p[2]*x)
fit = curve_fit(model, x, y, [1.0, 1.0])
beta = fit.param # best fit parameters
r = fit.resid # vector of residuals
J = fit.jacobian
=#

scatter(mu_all, L_all)#, label="naměřené hodnoty"
xlabel!("mu_a")
ylabel!("Populace")
legend!()


#PGFPlots.savefig("myfile.tex", backend_object(p), include_preamble=false)

