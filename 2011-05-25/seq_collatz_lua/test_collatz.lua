require "mgunit"
assert(loadfile "collatz.lua")()


mgunit.TestCase:new {
    name = "TestCollatz",

    test_2 = function(self)
        local entrada = 2
        local saida_esperada = { 2, 1 }
        local saida = collatz(entrada)
        self:assertequal(saida, saida_esperada)
    end,

    test_4 = function(self)
        local entrada = 4
        local saida_esperada = { 4, 2, 1 }
        local saida = collatz(entrada)
        self:assertequal(saida, saida_esperada)
    end,

    test_8 = function(self)
        local entrada = 8
        local saida_esperada = { 8, 4, 2, 1 }
        local saida = collatz(entrada)
        self:assertequal(saida, saida_esperada)
    end,

    test_6 = function(self)
        local entrada = 6
        local saida_esperada = { 6, 3, 10, 5, 16, 8, 4, 2, 1 }
        local saida = collatz(entrada)
        self:assertequal(saida, saida_esperada)
    end,

    test_13 = function(self)
        local entrada = 13
        local saida_esperada = { 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 }
        local saida = collatz(entrada)
        self:assertequal(saida, saida_esperada)
    end,
        
}

mgunit.main()
