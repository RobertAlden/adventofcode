include("../../../../lib/Julia/AoC_Utils.jl")
using .AoC_Utils: chunk_items, splitmap, memoize


function silver(data)
  
end

function gold(data)

end

const test = readlines("data/2022/day07/test.txt")
const data = readlines("data/2022/day07/input.txt")

@time println(silver(test))
@time println(gold(test))

@time println("Silver: $(silver(data))")
@time println("Gold: $(gold(data))")
