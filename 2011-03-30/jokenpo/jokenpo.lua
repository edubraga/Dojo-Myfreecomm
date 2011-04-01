local possibilidades = { pedra = 0, papel = 1, tesoura = 2 }


function jokenpo(primeiro, segundo)
    local vp, vs, result, lista_possibilidades
    vp = possibilidades[primeiro]
    vs = possibilidades[segundo]

    result = (vp - vs) % 3
    lista_possibilidades = {[0] = "empate", [1] = primeiro, [2] = segundo}

    return lista_possibilidades[result]
end

