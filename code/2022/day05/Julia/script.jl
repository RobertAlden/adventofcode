using Base.Iterators: take, drop

include("../../../../lib/Julia/AoC_Utils.jl")
using .AoC_Utils: parse_into_struct, chunk_items

struct Command
    quantity::Int
    from::Int
    to::Int
end

function silver(data::Array{String,1})
    crates_text, commandstrings = chunk_items(data, "")
    M = [crates_text[i][k] for i in eachindex(crates_text), k in 2:4:length(crates_text[1])]
    d = length(crates_text) - 1
    crates = map(filter(!=(' ')), eachcol(M[1:d, :]))

    for command in parse_into_struct.(commandstrings, Command)
        payload = reverse(collect(take(crates[command.from], command.quantity)))
        crates[command.from] = collect(drop(crates[command.from], command.quantity))
        crates[command.to] = vcat(payload, crates[command.to])
    end
    join(popfirst!.(crates))
end

function gold(data::Array{String,1})
    crates_text, commandstrings = chunk_items(data, "")
    M = [crates_text[i][k] for i in eachindex(crates_text), k in 2:4:length(crates_text[1])]
    d = length(crates_text) - 1
    crates = map(filter(!=(' ')), eachcol(M[1:d, :]))

    for command in parse_into_struct.(commandstrings, Command)
        payload = collect(take(crates[command.from], command.quantity))
        crates[command.from] = collect(drop(crates[command.from], command.quantity))
        crates[command.to] = vcat(payload, crates[command.to])
    end
    join(popfirst!.(crates))
end

const test = readlines("data/2022/day05/test.txt")
@time println(silver(test))
@time println(gold(test))

const data = readlines("data/2022/day05/input.txt")
@time println("Silver: $(silver(data))")
@time println("Gold: $(gold(data))")
@btime silver(data)
@btime gold(data)

