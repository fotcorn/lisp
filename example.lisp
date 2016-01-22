(def adder (fn [x]
    (fn [y] (+ x y))
))

(def addfive (adder 5))

(def addnine (adder 9))

(println (addfive 10))
(println (addnine 2))
