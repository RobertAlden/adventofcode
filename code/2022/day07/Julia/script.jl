

struct dir
    size::Int
    name::String
    contents::Array{dir,1}
end

function silver(data)

end

function gold(data)

end


test = readlines("data/2022/day07/test.txt")
input = readlines("data/2022/day07/input.txt")

@time println(silver(test))
@time println(gold(test))

@time println("Silver: $(silver(data))")
@time println("Gold: $(gold(data))")

@btime silver(data)
@btime gold(data)
