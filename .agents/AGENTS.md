# Agent Rules

## Git Branch Constraints
- **Rule**: ห้ามทำงาน, แก้ไขโค้ด, หรือ commit บน branch `main` โดยเด็ดขาด ต้องทำงานบน branch สำหรับฟีเจอร์ใหม่หรือ branch อื่นที่แยกออกมาเท่านั้น (เช่น `feature/...` หรือ branch ที่ตั้งขึ้นมาเฉพาะกิจ) หากตรวจสอบพบว่าอยู่ที่ branch `main` ให้ทำการ checkout ไปยัง branch ใหม่ทันทีก่อนเริ่มแก้ไขโค้ด
