import sqlite3
conn=sqlite3.connect('Youtube_videos.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS videos(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
time TEXT NOT NULL)
''')
def list_videos():
    cursor.execute("select * from  videos")
    for row in cursor.fetchall():
        print(row)
def add_video(name,time):
    cursor.execute("Insert into videos (name,time) values(?,?)",(name,time))
    print("Added SUccessfully!")
    conn.commit()
def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("Delete from videos where id=?",(video_id,))
    conn.commit()
def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3.  Update Videos")
        print("4.  Delete Videos")
        print("5.  Exit")
        choice=input("Enter your choice (1-5):")
        if choice=="1":
            list_videos()
        elif choice=="2":
            name=input("Enter the video name: ")
            time=input("Enter the Video time: ")
            add_video(name,time)
        elif choice=="3":
            video_id=input("Enter Video ID to update:")
            name=input("Enter the video name: ")
            time=input("Enter the Video time: ")
            update_video(video_id,name,time)
        elif choice=="4":
            video_id=input("Enter video_id to delete: ")
            delete_video(video_id)
        elif choice=="5":
            break
        else:
            print("Invalid Choice!")
    conn.close()
if __name__=="__main__":
    main()