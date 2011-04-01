require "mgunit"

assert(loadfile "jokenpo.lua")()


mgunit.TestCase:new {
    name = "TestJokenPo",

    test_pedra_pedra = function(self)
        local resultado, esperado
        resultado = jokenpo("pedra", "pedra")
        esperado = "empate"
        self:assertequal(resultado, esperado)
    end,

    test_pedra_papel = function(self)
        local resultado, esperado
        resultado = jokenpo("pedra", "papel")
        esperado = "papel"
        self:assertequal(resultado, esperado)
    end,

    test_pedra_tesoura = function(self)
        local resultado, esperado
        resultado = jokenpo("pedra", "tesoura")
        esperado = "pedra"
        self:assertequal(resultado, esperado)
    end,

    test_papel_papel = function(self)
        local resultado, esperado
        resultado = jokenpo("papel", "papel")
        esperado = "empate"
        self:assertequal(resultado, esperado)
    end,

    test_papel_tesoura = function(self)
        local resultado, esperado
        resultado = jokenpo("papel", "tesoura")
        esperado = "tesoura"
        self:assertequal(resultado, esperado)
    end,

    test_papel_pedra = function(self)
        local resultado, esperado
        resultado = jokenpo("papel", "pedra")
        esperado = "papel"
        self:assertequal(resultado, esperado)
    end,

    test_tesoura_tesoura = function(self)
        local resultado, esperado
        resultado = jokenpo("tesoura", "tesoura")
        esperado = "empate"
        self:assertequal(resultado, esperado)
    end,

    test_tesoura_pedra = function(self)
        local resultado, esperado
        resultado = jokenpo("tesoura", "pedra")
        esperado = "pedra"
        self:assertequal(resultado, esperado)
    end,

    test_tesoura_papel = function(self)
        local resultado, esperado
        resultado = jokenpo("tesoura", "papel")
        esperado = "tesoura"
        self:assertequal(resultado, esperado)
    end,
}


mgunit.main()
