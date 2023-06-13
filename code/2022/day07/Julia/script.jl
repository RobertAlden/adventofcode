include("../../../../lib/Julia/AoC_Utils.jl")
using .AoC_Utils: chunk_items

function parse(data)
    dirs = findall(x -> contains(x, " cd "), data)
    dirs = filter(x -> !contains(x, ".."), data[dirs])
    dirs = @. collect(last(split(dirs, " cd ")))

    contents = chunk_items(data, x -> startswith(x, "\$"))
    cleanup(str) = startswith(str, "dir") ? last(split(str, " ")) : first(split(str, " "))
    contents = map(x -> cleanup.(x), contents)

    zip(dirs, contents)
end

function silver(data)
    dir_tree = Dict(parse(data))

end

function gold(data)

end


test = readlines("data/2022/day07/test.txt")
data = readlines("data/2022/day07/input.txt")

@time println(silver(test))
@time println(gold(test))

# @time println("Silver: $(silver(data))")
# @time println("Gold: $(gold(data))")

# @btime silver(data)
# @btime gold(data)
