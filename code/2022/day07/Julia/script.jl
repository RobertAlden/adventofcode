include("../../../../lib/Julia/AoC_Utils.jl")
using .AoC_Utils: chunk_items, splitmap, memoize

function parse(data)
    dirstack = Vector{Int}()
    dirs = Vector{Int}()
    for line in data
        occursin(r"^(\$ ls|dir)", line) && continue
        if startswith(line, "\$ cd ..")
            push!(dirs, pop!(dirstack))
            continue
        end
        if startswith(line, "\$ cd ")
            push!(dirstack, 0)
            continue
        end
        dirstack .+= tryparse(Int, first(split(line, " ")))
    end
    vcat(dirs, dirstack)
end

function silver(data)
    dirs = parse(data)
    sum(filter(<=(100000), dirs))
end

function gold(data)
    dirs = parse(data)
    needed = 30000000 - (70000000 - maximum(dirs))
    minimum(filter(>=(needed), dirs))
end


const test = readlines("data/2022/day07/test.txt")
const data = readlines("data/2022/day07/input.txt")

@time println(silver(test))
@time println(gold(test))

@time println("Silver: $(silver(data))")
@time println("Gold: $(gold(data))")
