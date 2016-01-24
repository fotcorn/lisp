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
(def l (list 1 2 3 4))

(println (first l))
(println (last l))

(println (head l))
(println (tail l))

# map lists
(println (list 1 2 3 4))

(println (map quad (list 1 2 3 4 5 6)))

(println (map (fn [v] (* v v)) (list 1 2 3 4 5 6)))


# closure
(def adder (fn [x]
    (fn [y] (+ x y))
))

(def addfive (adder 5))

(def addnine (adder 9))

(println (addfive 10))
(println (addnine 2))


# boolean variables
(println true)
(println false)

(def a true)
(println a)
(println (not a))

# condition test
(def b 9)
(println (if (< b 5) "b is smaller than 5" "b is bigger or equal to 5"))
