# basics
(+ 1 2 3)
(println (+ 1 2 3))
(println "Hello World!")
(println 1 2 3)
(println (+ 1 (+ 2 8)))


# simple variable tests
(def a 5)
(def x (+ a 10))


# functions
(println ((fn [v] (* v v)) 5))

(println ((fn [a, b] (* a b)) 5 8))

(def five (fn [] 5))
(println (five))

(def hello (fn [] "Hello world"))

(def quad (fn [x] (* x x)))

(println (quad 5))

(println ((fn [x] (* x x)) 5))  # execute inline defined function

# lists
(println (list 1 2 3 4))

(println (map quad (list 1 2 3 4 5 6)))

(println (map (fn [v] (* v v)) (list 1 2 3 4 5 6)))


# closure
(def adder (fn [x]
    (fn [y] (+ x y))
))

(def addfive (adder 5))

(println (addfive 10))


# condition test
(println (if (< a 5) "A is smaller than 5" "A is bigger or equal to 5"))
