module AoC_Utils

export windowed, parse_into_struct, chunk_items, splitmap, memoize

windowed(arr, n) = [arr[i:(i+n-1)] for i in firstindex(arr):lastindex(arr)-n+1]

function parse_into_struct(str::String, datatype, seps::String=nothing)
    ### Parse a string into a struct, using the field types as a guide
    if isnothing(seps)
        seps = " "
    end

    types = [fieldtypes(datatype)...]
    substrings = collect(eachsplit(str, x -> contains(seps, x)))

    values = []
    for substring in substrings
        result = tryparse(first(types), substring)
        isnothing(result) && continue
        popfirst!(types)
        push!(values, result)
    end
    if length(values) < length(types)
        error("Insufficient number of valid values to
               populate struct fields. \nFields: $(types), Values: $(values)")
    end
    datatype(values...)
end

function chunk_items(data, f, dropempty=true)
    ### Divide a collection into chunks based on a boolean function
    indices = findall(f, data)
    if length(indices) == 0
        return [data]
    end
    indices = [firstindex(data) - 1; indices; lastindex(data) + 1]
    results = [data[indices[i]+1:indices[i+1]-1] for i in firstindex(indices):lastindex(indices)-1]
    dropempty ? collect(filter(x -> !isempty(x), results)) : collect(results)
end

function splitmap(f, coll; qualifer=nothing)
    if qualifer === nothing
        qualifer = x -> x == true
    end
    somethings = f.(filter(x -> qualifer(f(x)) == true, coll))
    nothings = filter(x -> qualifer(f(x)) == false, coll)
    somethings, nothings
end

function memoize(f)
    ### Memoize a function
    cache = Dict()

    function memoized_f(x...)
        if haskey(cache, x)
            return cache[x]
        else
            result = f(x...)
            cache[x] = result
            return result
        end
    end

    return memoized_f
end

end