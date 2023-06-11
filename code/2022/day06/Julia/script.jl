const data = readline("data/2022/day06/input.txt")
const test = readline("data/2022/day06/test.txt")

windowed(arr, n) = @views [arr[i:(i+n-1)] for i in firstindex(arr):lastindex(arr)-n+1]
function solution(n)
    distinct(x) = length(x) == length(Set(x))
    findfirst(distinct, windowed(data, n)) + n - 1
end

function silver(data)
    solution(4)
end

function gold(data)
    solution(14)
end

@time println(silver(test))
@time println(gold(test))

@time println("Silver: $(silver(data))")
@time println("Gold: $(gold(data))")

@btime silver(data)
@btime gold(data)
