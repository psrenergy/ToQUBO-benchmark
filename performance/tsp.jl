using CSV
using JuMP
using ToQUBO
using Anneal

function tsp(n::Int)
    t₀ = @timed begin
        model = Model(() -> ToQUBO.Optimizer(ExactSampler.Optimizer))

        @variable(model, x[1:n, 1:n], Bin, Symmetric)

        @constraint(model, [i in 1:n], sum(x[i,1:n]) == 2)
        @constraint(model, [i in 1:n], sum(x[i,i]) == 0)

        D = fill(10, (n,n))

        @objective(model, Min, sum(D .* x)/2)

    end

    t₁ = @timed begin
        qubo_model = ToQUBO.toqubo(JuMP.backend(model).model_cache)
        Q, α, β = ToQUBO.qubo(qubo_model)
    end

    return t₀.time, t₁.time
end


function measure(n::Int)
    
    println("Variables: $(n*n)")
    t₀, t₁ = tsp(n)
    println("Model: $(t₀)")
    println("Convert to QUBO: $(t₁)")
    println("Total elapsed time: $(t₀ + t₁)")
    println("----------")
   
end