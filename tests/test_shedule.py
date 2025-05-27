from zoneinfo import ZoneInfo
from db import Session
from models import User, Lesson, Booking
from datetime import datetime


def add_nine_bookings(lesson_id):
    session = Session()

    # Найти урок
    lesson = session.query(Lesson).filter_by(id=lesson_id).first()
    if not lesson:
        print(f"Lesson with id={lesson_id} not found")
        return

    # Выбрать 10 разных пользователей (с ролью 'user')
    users = session.query(User).filter(User.role == "user").limit(10).all()
    if len(users) < 10:
        print("В базе меньше 10 обычных пользователей")
        session.close()
        return

    # Создать бронирования
    for u in users:
        # Проверяем, что пользователь ещё не записан
        exists = (
            session.query(Booking).filter_by(user_id=u.id, lesson_id=lesson.id).first()
        )
        if not exists:
            booking = Booking(
                user_id=u.id,
                lesson_id=lesson.id,
                booked_at=datetime.now(ZoneInfo("Europe/Moscow")),
            )
            session.add(booking)

    # Обновляем счётчик текущих участников
    session.flush()  # чтобы все Booking получили id
    lesson.current_participants = (
        session.query(Booking).filter_by(lesson_id=lesson.id).count()
    )

    session.commit()
    print(
        f"Добавлено бронирований для урока {lesson_id}. Сейчас участников: {lesson.current_participants}"
    )
    session.close()


if __name__ == "__main__":
    # Замените 10 на ID вашего урока
    add_nine_bookings(lesson_id=3)
