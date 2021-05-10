def bmi4():
    datos=pd.read_csv("original.csv",header=0)
    X=datos[['resid_area','air_qual','room_num','age','dist1','dist2','dist3','dist4']]
    Y=datos["price"]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)
    lr=LinearRegression()
    lr.fit(X_train,Y_train)
    prediccion=lr.predict(X_test)
def bmi3():
    resi=input("Ingresa el area",type=FLOAT)
    air=input("Ingresa el air_qual",type=FLOAT)
    room=input("Ingresa el room_num",type=FLOAT)
    age=input("Ingresa la edad del producto",type=FLOAT)
    dist1=input("Ingresa la dist1: ",type=FLOAT)
    dist2=input("Ingresa la dist2: ",type=FLOAT)
    dist3=input("Ingresa la dist3: ",type=FLOAT)
    dist4=input("Ingresa la dist4: ",type=FLOAT)
    resp=lr.predict([[resi,air,room,age,dist1,dist2,dist3,dist4]])
    put_text("La respuesta es: " + str(resp))
if __name__ == '__main__':
    bmi2()
    bmi3()