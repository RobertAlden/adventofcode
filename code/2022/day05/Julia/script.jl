

struct Command
    quantity::Int
    from::Int
    to::Int
end

function parse_into_struct(datatype, str, sep)
    types = [fieldtypes(datatype)...]
    substrings = split(str, sep)
    values = []
    for str in substrings
        result = tryparse(first(types), str)
        isnothing(result) && continue
        popfirst!(types)
        push!(values, result)
    end
    if length(values) < length(types)
        error("Insufficient number of valid values to 
               populate struct fields. Fields: $(types) Values found: $(values)")
    end
    datatype(values...)
end

function chunk_items(data, sep)
    indices = findall(x -> x == sep, data)
    if length(indices) == 0
        return [data]
    end
    indices = [0; indices; length(data)]
    [data[indices[i]+1:indices[i+1]-1] for i in 1:length(indices)-1]
end

function silver(data::Array{String,1})
    crates, commandstrings = chunk_items(data, "")
    M = [crates[i][k] for i in eachindex(crates), k in 2:4:length(crates[1])]
    crates = eachcol(M[1:3, :])
    commands = parse_into_struct.(Command, commandstrings, " ")
end

function gold(data::Array{String,1})

end

const test = readlines("data/2022/day05/test.txt")
@time println(silver(test))
# @btime gold(test)

# data = readlines("data/2022/day05/input-[HIDE]-.txt")
# @time println(silver(data))
# @time println(gold(data))

parse_into_struct(Command, "move 8 from 9 to 6", " ")