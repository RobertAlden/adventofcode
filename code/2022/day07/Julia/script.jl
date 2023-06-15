include("../../../../lib/Julia/AoC_Utils.jl")
using .AoC_Utils: chunk_items

function parse(data)
    dirs = findall(x -> contains(x, " cd "), data)
    dirs = filter(x -> !contains(x, ".."), data[dirs])
    dirs = last.(split.(dirs, " cd "))

    contents = chunk_items(data, x -> startswith(x, "\$"))

    cleanup(str) = startswith(str, "dir") ? last(split(str, " ")) : first(split(str, " "))
    contents = map.(cleanup, contents)

    collect(zip(dirs, contents))
end

function splitmap(f, coll)
    somethings = f.(filter(x -> !isnothing(f(x)), coll))
    nothings = filter(x -> isnothing(f(x)), coll)
    somethings, nothings
end

function compute_node(tree, node)
    dir_contents, sub_dirs = splitmap(x -> tryparse(Int, x), tree[node])
    isempty(sub_dirs) && return sum(dir_contents)
    dir_size = isempty(dir_contents) ? 0 : sum(dir_contents)
    dir_size + sum(map(x -> compute_node(tree, x), sub_dirs))
end

function silver(data)
    dir_tree = parse(data)
    # dir_sizes = map(x -> compute_node(dir_tree, x), dir_tree)
    # sum(filter(x -> x <= 100000, dir_sizes))
end

function gold(data)
    dir_tree = parse(data)
    dir_sizes = sort(map(x -> compute_node(dir_tree, x), collect(keys(dir_tree))))
    dir_capacity = 70000000
    goal = dir_capacity - sum(dir_sizes)
    dir_sizes[findfirst(x -> x >= goal, dir_sizes)]
end


const test = readlines("data/2022/day07/test.txt")
const data = readlines("data/2022/day07/input.txt")

@time println(silver(test))
# @time println(gold(test))

@time println("Silver: $(silver(data))")
# @time println("Gold: $(gold(data))")

# @btime silver(data)
# @btime gold(data)
