# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)\n"

round(df[df['population'] <= 500]['median_house_value'].mean(), 2),
{
    "metadata":
    {
        "collapsed": false
    }
}
"cell_type": "code",
  "execution_count": 12,
   "outputs":
        {
            "data": {
                "text/plain": "4.0"
                },
            "execution_count": 12,
         "metadata": {},
         "output_type": "execute_result"
        }
    "source":
