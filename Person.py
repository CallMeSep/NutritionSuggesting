# Revised Harris-Benedict Equation:
# For men:
# BMR = 66.5 + ( 13.76 × weight in kg ) + ( 5.003 × height in cm ) – ( 6.755 × age in years )
# For women:
# BMR = 9.247W + 3.098H - 4.330A + 447.593
import pandas as pd
import numpy as np
df = pd.read_excel("output.xlsx")
# feat = ['Thực Phẩm', ]
class Profile:
    def __init__(self, height, weight, age, gender, disease, meal,df):
        self.weight = weight
        self.height = height
        self.gender = gender
        self.age = age
        self.meal = meal
        self.calories = 0
        self.bmi = self.weight / ((self.height / 100) ** 2)
        self.df = df
        if self.gender == 'Male':
            self.calories = 66.5 + (13.76 * (self.weight)) + (5.003 * (self.height)) - (6.755 * self.age)
        elif self.gender == 'Female':
            self.calories = 9.247 * self.weight + 3.098 * self.height - 4.330 * self.age + 447.593

        if self.bmi < 18.5:
            self.calories = self.calories * 1.10
        elif 18.5 <= self.bmi <= 24.9:
            self.calories = self.calories
        elif 25 <= self.bmi <= 29.9:
            self.calories = self.calories * 0.9
        elif 30 <= self.bmi < 39.9:
            self.calories = self.calories * 0.85
        else:
            self.calories = self.calories * 0.8

        self.disease = disease

    def meal_cal(self):
        if self.disease == 'Tieu duong':
            # bo xung chat xo, chat beo thuc vat
            self.protein = ((0.45 * self.calories) / 4) / self.meal
            self.fat = ((0.2 * self.calories) / 9) / self.meal
            self.carb = ((0.35 * self.calories) / 4) / self.meal

            chatdam = df[(df['Loại'] == 'Thịt đỏ')|(df['Loại'] == 'Thịt trắng') | (df['Loại'] == 'Hải sản')].sample(n=5)
            tinhbot = df[df['Loại'] == 'Tinh bột'].sort_values(by='Total dietary fiber(Gms)', ascending=False).head(
                15).sample(n=5)
            trangmieng = df[df['Loại'] == 'Hoa quả'].sort_values(by='Vitamin A(IU )', ascending=False).head(
                15).sample(n=5)
            rau = df[df['Loại'] == 'Rau'].sort_values(by='Vitamin A(IU )', ascending=False).head(15).sample(5)

            chatdam['Khẩu phần (gam)'] = ((self.protein / chatdam['Protein(Gms)']) * 100).apply(np.floor)
            tinhbot['Khẩu phần (gam)'] = ((self.carb / tinhbot['Carbohydrate, by diff.(Gms)']) * 100).apply(np.floor)
            trangmieng['Khẩu phần (gam)'] = (((self.carb * 0.25) / trangmieng['Carbohydrate, by diff.(Gms)']) * 100).apply(
                np.floor)


        elif self.disease == 'Gout':
            # bo sung nuoc, vitamin A, chat so, dam thuc vat
            self.protein = ((0.2 * self.calories) / 4) / self.meal
            self.fat = ((0.2 * self.calories) / 9) / self.meal
            self.carb = ((0.60 * self.calories) / 4) / self.meal
            chatdam = df[(df['Loại'] == 'Thịt trắng') | (df['Loại'] == 'Hải sản')].sample(n=5, )
            tinhbot = df.loc[
                (df['Loại'] == 'Tinh bột') & (df['Carbohydrate, by diff.(Gms)'] / df['Protein(Gms)'] >= 2.5) & (
                            df['Carbohydrate, by diff.(Gms)'] / df['Protein(Gms)'] <= 3.5)]
            tinhbot = tinhbot.sort_values(by='Protein(Gms)', ascending=False).head(15).sample(n=5)
            #             tinhbot = tinhbot.loc(tinhbot['Loại'] == 'Tinh bột')
            trangmieng = df[df['Loại'] == 'Hoa quả'].sample(n=5, )
            rau = df[df['Loại'] == 'Rau'].sort_values(by='Vitamin A(IU )', ascending=False).head(15).sample(5)

            chatdam['Khẩu phần (gam)'] = ((self.protein / chatdam['Protein(Gms)']) * 100).apply(np.floor)
            tinhbot['Khẩu phần (gam)'] = (((self.carb * 0.75) / tinhbot['Carbohydrate, by diff.(Gms)']) * 100).apply(np.floor)
            trangmieng['Khẩu phần (gam)'] = (((self.carb * 0.25) / trangmieng['Carbohydrate, by diff.(Gms)']) * 100).apply(
                np.floor)


        elif self.disease == 'Tao bon':
            # Bo sung chat so hoa qua
            self.protein = ((0.20 * self.calories) / 4) / self.meal
            self.fat = ((0.2 * self.calories) / 9) / self.meal
            self.carb = ((0.60 * self.calories) / 4) / self.meal

            chatdam = df[(df['Loại'] == 'Thịt đỏ')|(df['Loại'] == 'Thịt trắng') | (df['Loại'] == 'Hải sản')].sample(n=5, )
            tinhbot = df[df['Loại'] == 'Tinh bột'].sort_values(by='Total dietary fiber(Gms)', ascending=False).head(
                15).sample(n=5, )
            trangmieng = df[df['Loại'] == 'Hoa quả'].sample(n=5, )
            rau = df[df['Loại'] == 'Rau'].sort_values(by='Total dietary fiber(Gms)', ascending=False).head(15).sample(5)
            chatdam['Khẩu phần (gam)'] = ((self.protein / chatdam['Protein(Gms)']) * 100).apply(np.floor)
            tinhbot['Khẩu phần (gam)'] = (((self.carb * 0.6) / tinhbot['Carbohydrate, by diff.(Gms)']) * 100).apply(np.floor)
            trangmieng['Khẩu phần (gam)'] = (((self.carb * 0.4) / trangmieng['Carbohydrate, by diff.(Gms)']) * 100).apply(
                np.floor)
        #             chatdam['Khẩu phần (gam)'] =  chatdam['Khẩu phần (gam)'].apply(np.floor)
        #             tinhbot['Khẩu phần (gam)'] = tinhbot['Khẩu phần (gam)'].apply(np.floor)
        #             trangmieng['Khẩu phần (gam)'] = trangmieng['Khẩu phần (gam)'].apply(np.floor)
        elif self.disease == 'Mo mau':
            # Bo sung chat so nen an hai san thay cho thit
            self.protein = ((0.3 * self.calories) / 4) / self.meal
            self.fat =( (0.3 * self.calories) / 9) / self.meal
            self.carb =( (0.4 * self.calories) / 4) / self.meal
            chatdam = df[(df['Loại'] == 'Thịt trắng') |(df['Loại'] == 'Hải sản')].sample(n=5)
            tinhbot = df[df['Loại'] == 'Tinh bột'].sort_values(by='Total dietary fiber(Gms)', ascending=False).head(
                15).sample(n=5, )
            trangmieng = df[df['Loại'] == 'Hoa quả'].sample(n=5)
            rau = df[df['Loại'] == 'Rau'].sort_values(by='Total dietary fiber(Gms)', ascending=False).head(15).sample(5)

            chatdam['Khẩu phần (gam)'] = ((self.protein / chatdam['Protein(Gms)']) * 100).apply(np.floor)
            tinhbot['Khẩu phần (gam)'] = (((self.carb * 0.8) / tinhbot['Carbohydrate, by diff.(Gms)']) * 100).apply(np.floor)
            trangmieng['Khẩu phần (gam)'] = (((self.carb * 0.2) / trangmieng['Carbohydrate, by diff.(Gms)']) * 100).apply(
                np.floor)


        elif self.disease == 'Thi giac':
            # Bo sung vitamin a vitamin e
            self.protein = ((0.2 * self.calories) / 4) / self.meal
            self.fat = ((0.2 * self.calories) / 9) / self.meal
            self.carb = ((0.6 * self.calories) / 4) / self.meal
            chatdam = df[(df['Loại'] == 'Thịt đỏ')|(df['Loại'] == 'Thịt trắng') | (df['Loại'] == 'Hải sản')].sort_values(by='Vitamin B12(Mcg)', ascending=False).head(
                15).sample(n=5)
            tinhbot = df[df['Loại'] == 'Tinh bột'].sort_values(by='Vitamin B6(Mg )', ascending=False).head(
                15).sample(n=5, )
            trangmieng = df[df['Loại'] == 'Hoa quả'].sort_values(by='Vitamin A(IU )', ascending=False).head(15).sample(n=5)
            rau = df[df['Loại'] == 'Rau'].sort_values(by='Vitamin A(IU )', ascending=False).head(15).sample(5)

            chatdam['Khẩu phần (gam)'] = ((self.protein / chatdam['Protein(Gms)']) * 100).apply(np.floor)
            tinhbot['Khẩu phần (gam)'] = (((self.carb * 0.8) / tinhbot['Carbohydrate, by diff.(Gms)']) * 100).apply(
                np.floor)
            trangmieng['Khẩu phần (gam)'] = (
                        ((self.carb * 0.2) / trangmieng['Carbohydrate, by diff.(Gms)']) * 100).apply(
                np.floor)
        elif self.disease == 'Loang xuong':
            # bo sung canxi nuoc, vitamin d
            self.protein = ((0.2 * self.calories) / 4) / self.meal
            self.fat = ((0.2 * self.calories) / 9) / self.meal
            self.carb = ((0.6 * self.calories) / 4) / self.meal
            chatdam = df[(df['Loại'] == 'Thịt đỏ')|(df['Loại'] == 'Thịt trắng') |(df['Loại'] == 'Hải sản')].sample(n=5)
            tinhbot = df[df['Loại'] == 'Tinh bột'].sort_values(by='Total dietary fiber(Gms)', ascending=False).head(
                15).sample(n=5, )
            trangmieng = df[(df['Loại'] == 'Hoa quả') | (df['Loại'] == 'Sản phẩm từ sữa')].sort_values(by='Calcium(Mg )').head(20).sample(n=5)
            rau = df[df['Loại'] == 'Rau'].sort_values(by='Vitamin A(IU )', ascending=False).head(15).sample(5)

            chatdam['Khẩu phần (gam)'] = ((self.protein / chatdam['Protein(Gms)']) * 100).apply(np.floor)
            tinhbot['Khẩu phần (gam)'] = (((self.carb * 0.8) / tinhbot['Carbohydrate, by diff.(Gms)']) * 100).apply(
                np.floor)
            trangmieng['Khẩu phần (gam)'] = (
                        ((self.carb * 0.2) / trangmieng['Carbohydrate, by diff.(Gms)']) * 100).apply(
                np.floor)

        return chatdam, tinhbot, trangmieng,rau
