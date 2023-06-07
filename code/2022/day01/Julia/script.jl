test = readlines("data/2022/day01/test.txt")
data = readlines("data/2022/day01/input-[HIDE]-.txt")

@views function listSplit(data, sep)
    indices = findall(x -> x == sep, data)
    if length(indices) == 0
        return [data]
    end
    indices = [0; indices; length(data)]
    [data[indices[i]+1:indices[i+1]-1] for i in 1:length(indices)-1]
end

function silver(data::Array{String,1})
    chunks = listSplit(data, "")
    map(chunk -> map(x -> parse(Int64, x), chunk) |> sum, chunks) |> maximum
end

function gold(data::Array{String,1})
    chunks = listSplit(data, "")
    inner = chunk -> map(x -> parse(Int64, x), chunk) |> sum
    map(inner, chunks) |> sort |> x -> last(x, 3) |> sum
end

@time println(silver(data))

@time println(gold(data))
