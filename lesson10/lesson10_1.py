def get_bmi():
    '''
    建立身高, 體重的輸入並計算 BMI
    return: (bmi_value, error_message)
    '''
    # 初始化回傳變數
    height = None
    weight = None
    
    try:
        height = float(input('請輸入身高 (120~250 cm): '))
        if not (120 <= height <= 250):
            raise ValueError('身高範圍輸入錯誤')

        weight = float(input('請輸入體重 (30~200 kg): '))
        if not (30 <= weight <= 200):
            raise ValueError('體重範圍輸入錯誤')
            
        # 只有在 try 區塊內一切正常，才會執行到這裡
        bmi = weight / ((height / 100) ** 2)
        return round(bmi, 2), None

    except ValueError as e:
        # 捕捉數值轉換錯誤或手動拋出的範圍錯誤
        return None, str(e)
    except Exception as e:
        # 捕捉其他非預期的錯誤
        return None, f"發生意外錯誤: {e}"


def get_status(BMI):
    '''
    根據BMI值，判斷體重狀態
    :param BMI: float, 計算出的BMI值
    '''

    print('你的 BMI 為:', round(BMI, 1))

    if BMI < 18.5:
        x = '體重過輕'
    elif 18.5 <= BMI < 24:
        x = '正常範圍'
    elif 24 <= BMI < 27:
        x = '體重過重'
    elif 27 <= BMI < 30:
        x = '輕度肥胖'
    elif 30 <= BMI < 35:
        x = '中度肥胖'
    else:
        x = '重度肥胖'

    print('您的體重狀態為：', x)


def main():
    while True:
        bmi, error = get_bmi()

        if error:
            print(f"輸入錯誤，請重新輸入：{error}")
        
        else:
            print(f"您的 BMI 為：{bmi}")
            get_status(bmi)
            print('--- 應用程式結束 ---')
            break
    print("程式結束")        


if __name__ == "__main__":
    main()