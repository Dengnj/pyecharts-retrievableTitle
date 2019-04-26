from pyecharts.charts import Parallel


def test_parallel_base():
    data = [
        [1, 91, 45, 125, 0.82, 34],
        [2, 65, 27, 78, 0.86, 45],
        [3, 83, 60, 84, 1.09, 73],
        [4, 109, 81, 121, 1.28, 68],
        [5, 106, 77, 114, 1.07, 55],
        [6, 109, 81, 121, 1.28, 68],
    ]
    c = (
        Parallel()
        .add_schema(
            [
                {"dim": 0, "name": "data"},
                {"dim": 1, "name": "AQI"},
                {"dim": 2, "name": "PM2.5"},
                {"dim": 3, "name": "PM10"},
                {"dim": 4, "name": "CO"},
                {"dim": 5, "name": "NO2"},
            ]
        )
        .add("parallel", data)
    )
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
