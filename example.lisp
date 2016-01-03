# function tests
(def five (fn [] 5))
(println (five))


(def quad (fn [x] (* x x)))

(println (quad 5))

(println ((fn [x] (* x x)) 5))  # execute inline defined function
