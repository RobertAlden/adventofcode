using Base.Iterators: partition

test = readlines("data/2022/day03/test.txt")
data = readlines("data/2022/day03/input-[HIDE]-.txt")

score(x::Char) = Int(x) - 96 < 0 ? Int(x) - 64 + 26 : Int(x) - 96

function silver(data::Array{String,1})
    function solution(backpack::String)
        size = length(backpack)
        contents = collect(partition(backpack, size ÷ 2))
        for i ∈ contents[1]
            i ∈ contents[2] && return i
        end
    end
    score.(map(solution, data)) |> sum
end

function gold(data::Array{String,1})
    groups = collect(partition(data, 3))
    function solution(group)
        for i ∈ group[1]
            i ∈ group[2] && i ∈ group[3] && return i
        end
    end
    score.(map(solution, groups)) |> sum
end

@btime silver(test)
@btime gold(test)

@btime silver(data)
@btime gold(data)
