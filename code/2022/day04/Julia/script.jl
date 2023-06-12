include("../../../../lib/Julia/AoC_Utils.jl")
using .AoC_Utils: parse_into_struct

struct RangeOverlap
    a1::Int
    a2::Int
    b1::Int
    b2::Int
end

contains(r::RangeOverlap) = r.a1 <= r.b1 && r.a2 >= r.b2 || r.b1 <= r.a1 && r.b2 >= r.a2
overlaps(r::RangeOverlap) = r.a1 <= r.b2 && r.b1 <= r.a2
solution(data, f) = count(f, parse_into_struct.(data, RangeOverlap, "-,"))

function silver(data)
    solution(data, contains)
end

function gold(data)
    solution(data, overlaps)
end

const test = readlines("data/2022/day04/test.txt")
const data = readlines("data/2022/day04/input.txt")

@time println(silver(test))
@time println(gold(test))

@time println("Silver: $(silver(data))")
@time println("Gold: $(gold(data))")

@btime silver(data)
@btime gold(data)
