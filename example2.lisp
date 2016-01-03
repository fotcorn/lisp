(+ 1 2 3)
(println (+ 1 2 3))
(def a 5)
(def x (+ a 10))

(defn x (fn [a b c] (block
    (println a)
    (println b)
    (println c)
)))

(def hello (fn [] "Hello world"))

(println "Hello World!")
(println 1 2 3)
(println (+ 1 (+ 2 8)))

(def a 123)
(println a)

(println (if (< a 5) "A is smaller than 5" "A is bigger or equal to 5"))

(list 1 2 3 4)

(println (map (fn [v] (* v v)) (list 1 2 3 4 5 6)))

(println ((fn [v] (* v v)) 5))
