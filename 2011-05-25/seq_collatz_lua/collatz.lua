function collatz(num, resposta)
    if not resposta then
        resposta = {}
    end
    
    table.insert(resposta, num)
    if num == 1 then
        return resposta
    elseif num % 2 == 0 then
        return collatz(num / 2, resposta)
    else
        return collatz(num * 3 + 1, resposta)
    end
end
