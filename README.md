# Running

Document my running training and do some ML on the data.

## Business Goals

1. Predict my 10.0km finishing time for the [Valentinslauf](https://www.valentinslauf.de) on Feb 20th, 2022 within 1 SD.
2. Predict my 21.1km finishing time for the [Berlin Halfmarathon](https://www.generali-berliner-halbmarathon.de/) on Apr 3rd, 2022 within 1 SD.

----

## Assumptions

* There is a linear relationship between the running time and the distance covered.
* To cover a distance of zero, I need exactly zero time (no time travel this time, sorry).

----

## The Model

Let's start with a simple linear model:

    time = m * dist

----

## Predictions

Predictions made on Jan 5th fro 3 observations:

* Valentinslauf:  71.69 min
* Halfmarathon : 151.28 min

Let's collect more data!

----

## Test Data

Coming with the real events.

----

## License

(c) 2021 Dr. Kristian Rother

Code is subject to the MIT License. See the LICENSE file for details.
