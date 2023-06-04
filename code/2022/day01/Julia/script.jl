using BenchmarkTools, AbbreviatedStackTraces

MODE = "test"

test = readlines("data/2022/day01/test.txt")
data = readlines("data/2022/day01/input-[HIDE]-.txt")

function listSplit(data, sep)
    bool_seq = [(i == sep) for i in data]
    seq = Vector{Vector{String}}()
    chunk = Vector{String}()
    for (b, v) in zip(bool_seq, data)
        if !b
            push!(chunk, v)
        else
            push!(seq, copy(chunk))
            empty!(chunk)
        end
    end
    push!(seq, chunk)
    seq
end

function silver(data::Array{String,1})
    chunks = listSplit(data, "")
    map(chunk->map(x -> parse(Int64, x), chunk) |> sum, chunks) |> maximum
end

function gold(data::Array{String,1})
    chunks = listSplit(data, "")
    inner = chunk->map(x -> parse(Int64, x), chunk) |> sum
    map(inner, chunks) |> sort |> x->last(x,3) |> sum
end

@time @show silver(test)
@time @show gold(test)

@time @show silver(data)
@time @show gold(data)
