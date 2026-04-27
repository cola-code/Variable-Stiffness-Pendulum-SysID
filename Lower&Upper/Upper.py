import serial
import csv
import time

#configuration
SERIAL_PORT = 'COM8' 
BAUD_RATE = 115200
CSV_FILENAME = 'data_r1.csv'
#-------------

def main():
    print(f"正在连接串口 {SERIAL_PORT} (波特率: {BAUD_RATE})...")
    try:
        # 打开串口
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    except serial.SerialException as e:
        print(f"串口打开失败: {e}\n请检查端口号或确认 Arduino 串口监视器已关闭！")
        return

    print(f"连接成功！开始记录数据到 {CSV_FILENAME} ...\n按 Ctrl+C 停止记录。")

    # 打开并准备写入 CSV
    with open(CSV_FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time_s', 'Pitch_deg']) # 写入表头

        try:
            while True:
                if ser.in_waiting > 0:
                    # 读取一行并解码
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if line:
                        try:
                            # 按照你的要求解析并转换单位
                            time_us_str, pitch_str = line.split(',')
                            time_s = float(time_us_str) / 1000000.0  # 微秒转秒
                            pitch = float(pitch_str)

                            # 写入 CSV 并打印在控制台
                            writer.writerow([f"{time_s:.6f}", pitch])
                            print(f"Time: {time_s:.6f} s | Pitch: {pitch:.2f}°")
                        
                        except ValueError:
                            # 过滤掉刚上电时的乱码或非标准输出
                            pass
                else:
                    time.sleep(0.001) # 防止死循环占满 CPU
                    
        except KeyboardInterrupt:
            print("\n检测到中止命令,数据采集已停止。")
        finally:
            ser.close()
            print("串口已关闭。")

if __name__ == '__main__':
    main()