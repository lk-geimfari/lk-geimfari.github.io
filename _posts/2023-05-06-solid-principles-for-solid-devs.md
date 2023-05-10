---
layout: post
title: SOLID Principles for solid developers.
date: 2023-05-06
preview_img: solid.png
description: In this article, we'll learn about SOLID principles and how to apply them in Python to write more flexible, maintainable, and scalable code.
published: true
starred: true
redirect_from:
  - /2023/05/solid-python/
---


Let me guess, you were browsing jobs on Linkedin and saw a requirement to understand **SOLID** principles and decided
to google what the heck SOLID is? Either way, you've come to the right place.

This article is not meant to be a SOLID-propaganda, and I'm not going to convince you that you are obligated to adhere
to SOLID principles. My purpose is simple — to tell you what SOLID is and how it works. It's up to you to apply these
principles in your work or not.

## Definition

In short, **SOLID** is a set of five principles of object-oriented design focused at making software more modular,
maintainable, and scalable.

The acronym **SOLID** stands for:

- **S** - Single Responsibility Principle (SRP)
- **O** - Open/Closed Principle (OCP)
- **L** - Liskov Substitution Principle (LSP)
- **I** - Interface Segregation Principle (ISP)
- **D** - Dependency Inversion Principle (DIP)

Let's examine each of these principles separately.

## Single Responsibility Principle

The Single Responsibility Principle (SRP) states that a class should have only one reason to change, meaning that it
should have only one responsibility or task to perform. By following this principle, a class's functionality is more
focused, leading to improved manageability and comprehension.

First, let's look at code which violates *SRP*:

```python
class User:
    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password

    def login(self) -> None:
        print(f"Logging in user: {self}")

    def logout(self) -> None:
        print(f"Logging out user: {self}")

    def send_notification(self, message) -> None:
        print(f"Sending notification to {self}: {message}")

    def serialize(self) -> None:
        print(f"Serializing user: {self}")
```

It's evident that the `User` class violates the *SRP* since it's accountable for numerous tasks, namely:

- Storing user information
- Authenticating users
- Sending notifications
- Serializing users

If any one of these responsibilities changes, it may affect the entire ``User`` class. For instance, if the method for
sending notifications needs to be updated or changed, it could potentially break the code for the entire ``User``
class, including the methods for logging in.

By following *SRP*, our goal is to separate the different responsibilities into their own classes, so that each class is
responsible for only one thing. For example, a ``User`` class could be responsible for storing user information only,
while separate `Authentication`, `NotificationSender`, and `UserSerializer` classes could be responsible for their
respective tasks.

Here's an example of how we can refactor the `User` class to adhere to the *SRP*:

```python
class User:
    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"

    def __repr__(self) -> str:
        return f"User('{self.email}')"


class UserSerializer:
    def __init__(self, user: User) -> None:
        self.user = user

    def serialize(self) -> None:
        print(f"Serializing user: {self.user}")


class Authentication:
    def login(self, user: User) -> None:
        print(f"Logging in user: {user}")

    def logout(self, user) -> None:
        print(f"Logging out user: {user}")


class NotificationSender:
    def send_notification(self, user: User, message: str) -> None:
        print(f"Sending notification to {user}: {message}")


if __name__ == "__main__":
    user = User(
        "Winston Churchill",
        "winston@churchill.uk",
        "we-shall-fight"
    )

    # Authentication
    auth = Authentication()
    auth.login(user)
    auth.logout(user)

    # Notification
    notification_sender = NotificationSender()
    notification_sender.send_notification(
        user, "Beware of the German U-boats!",
    )

    # Serialization
    user_serializer = UserSerializer(user)
    user_serializer.serialize()
```

## Open/Closed Principle

The Open/Closed Principle (OCP) states that a class should be open for extension but closed for modification. This means
that we should be able to add new functionality to a class without changing its existing code.

Let's examine the code that violates the *OCP*:

```python
class NotificationService:
    def __init__(self, notification: str) -> None:
        self.notification = notification

    def send_notification(self, message: str) -> None:
        if self.notification == "email":
            print(f"Sending email with message: {message}")
        elif self.notification == "push":
            print(f"Sending SMS with message: {message}")
        elif self.notification == "slack":
            print(f"Sending whatsapp with message: {message}")


if __name__ == "__main__":
    notification_service = NotificationService("slack")
    notification_service.send_notification("Hello World")
```

This code violates the *OCP* because the `NotificationService` class is not closed for modification. If we want to
add a new notification method, we have to modify the existing code in the `send_notification` method.

Let's modify the code to follow to the OCP:

```python
import abc


class Notification(abc.ABC):

    @abc.abstractmethod
    def send(self, message: str) -> None:
        raise NotImplementedError


class PushNotification(Notification):
    def send(self, message: str) -> None:
        print("Sending push notification...")


class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print("Sending email notification...")


class SlackNotification(Notification):
    def send(self, message: str) -> None:
        print("Sending slack notification...")


class NotificationService:
    def __init__(self, notification: Notification) -> None:
        self.notification = notification

    def send_notification(self, message: str) -> None:
        self.notification.send(message)


if __name__ == "__main__":
    notification_service = NotificationService(SlackNotification())
    notification_service.send_notification("German U-boats spotted!")
```

In this example, the `NotificationService` class is closed for modification because we can add new notification
methods without changing the existing code. For instance, if we want to add a new `SMSNotification` class, we can
simply create a new class that extends the `Notification` class and implement the `send` method. Such design
allows us to add new notification methods without changing the existing code.

## Liskov Substitution Principle

The LSP states that a subclass should be substitutable for its superclass without changing the correctness of the
program. In other words, if we replace an instance of a superclass with an instance of its subclass, the program should
still behave correctly.

Let's take a look at the following example which violates the *LSP*:

```python
import abc


class ICharacter(abc.ABC):
    @abc.abstractmethod
    def greet(self) -> None:
        raise NotImplementedError


class Human(ICharacter):
    def greet(self) -> None:
        print("Hello, I am a human")


class Kazakh(Human):
    def greet(self) -> None:
        print("Здарова, заебал.")


class French(Human):
    def greet(self) -> None:
        print("Bonjour!")


class German(Human):
    def greet(self) -> None:
        raise RuntimeError("Nien!")
```

In this example, the `German` class is a subclass of ``Human``. However, it violates the *LSP* because it
changes the behavior of the `German`. The `Human` class can greet, but the `German` class cannot. This means
that code that expects a `Human` instance may behave unexpectedly or fail when given a `German` instance.

Let's refactor code to make it follow *LSP*:

```python
import abc


class ICharacter(abc.ABC):
    @abc.abstractmethod
    def greet(self) -> None:
        raise NotImplementedError


class Human(ICharacter):
    def greet(self) -> None:
        print("Hello, I am a human")


class Kazakh(Human):
    def greet(self) -> None:
        print("Здорова, заебал.")


class French(Human):
    def greet(self) -> None:
        print("Bonjour!")


class German(Human):
    def greet(self) -> None:
        print("Hallo!")
```

## Interface Segregation Principle

The Interface Segregation Principle (ISP) states that a class shouldn't be forced to depend on methods it does not use.
In other words, we should break down large interfaces into smaller ones, more focused on the needs of each class.

Let's take a look at the following example which violates the *ISP*:

```python
import abc


class ICharacter(abc.ABC):
    @abc.abstractmethod
    def attack(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def walk(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def pull_out_rpg(self) -> None:
        raise NotImplementedError


class Warrior(ICharacter):
    def attack(self) -> None:
        print("Warrior is attacking")

    def walk(self) -> None:
        print("Warrior is walking")

    def pull_out_rpg(self) -> None:
        print("Pulling out motherfucking RPG-7")


class Civilian(ICharacter):

    def pull_out_rpg(self) -> None:
        # Jesus Christ, what kind of civilian is this?
        print("Pulling out motherfucking RPG-7")

    def attack(self) -> None:
        # Why the hell would a civilian attack?
        print("Civilian is attacking")

    def walk(self) -> None:
        print("Civilian is walking")

```

In this example, we define an `ICharacter` interface that has three methods:

- ``attack``
- ``walk``
- ``pull_out_rpg``

We have a violation of the *ISP* in the implementation of the `ICharacter` interface, where we
define two concrete classes `Warrior` and `Civilian`. The problem is that `Civilian` is forced to implement the `attack`
and `pull_out_rpg` methods, even though it may not (haha) need to use them.

If we don't implement these methods in the `Civilian` class, we'll get an error:

```text
TypeError: Can't instantiate abstract class Civilian with abstract methods attack, pull_out_rpg
```

To avoid this kind of problems, it's highly recommendable to break down large interfaces into smaller ones, more focused
on the needs of each class. Let's refactor the code to make it follow *ISP*:

```python
import abc


class ICharacter(abc.ABC):

    @abc.abstractmethod
    def walk(self) -> None:
        raise NotImplementedError


class IWarrior(ICharacter):

    @abc.abstractmethod
    def attack(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def pull_out_rpg(self) -> None:
        raise NotImplementedError


class Warrior(IWarrior):
    def attack(self) -> None:
        print("Warrior is attacking")

    def walk(self) -> None:
        print("Warrior is walking")

    def pull_out_rpg(self) -> None:
        print("Pulling out motherfucking RPG-7")


class Civilian(ICharacter):

    def walk(self) -> None:
        print("Civilian is walking")
```

Now we no longer arm civilians with hand-held anti-tank grenade launchers and the world is a little safer place to live.

## Dependency Inversion Principle

The Dependency Inversion Principle (DIP) states that high-level classes should not depend on low-level classes. Instead,
they should both depend on abstractions. Abstractions should not depend on details, but details should depend on
abstractions.

Let's examine *DIP* violation:

```python
class StripePaymentGateway:
    def pay(self) -> None:
        print("Paying with Stripe")


class KlarnaPaymentGateway:
    def pay(self) -> None:
        print("Paying with Klarna")


class BitPayPaymentGateway:
    def pay(self) -> None:
        print("Paying with BitPay")


class PaymentProcessor:
    def __init__(self) -> None:
        self.stripe = StripePaymentGateway()
        self.klarna = KlarnaPaymentGateway()
        self.bitpay = BitPayPaymentGateway()

    def process_payment(self, payment_gateway: str) -> None:
        if payment_gateway == "stripe":
            self.stripe.pay()
        elif payment_gateway == "klarna":
            self.klarna.pay()
        elif payment_gateway == "bitpay":
            self.bitpay.pay()


if __name__ == "__main__":
    payment_processor = PaymentProcessor()
    payment_processor.process_payment('stripe')
    payment_processor.process_payment('klarna')
    payment_processor.process_payment('bitpay')
```

In this example, we have a `PaymentProcessor` class which has a hard dependencies on concrete implementations of payment
gateways. This is a violation of the *DIP* because the `PaymentProcessor` class is a high-level class that depends on
low-level classes. This means that if we want to add a new payment gateway, we'll have to modify the `PaymentProcessor`
class which potentially can break the code.

Let's refactor our payment gateway to make it follow *DIP*:

```python
import abc


class PaymentGateway(abc.ABC):
    @abc.abstractmethod
    def pay(self) -> None:
        raise NotImplementedError


class StripePaymentGateway(PaymentGateway):
    def pay(self) -> None:
        print("Paying with Stripe")


class KlarnaPaymentGateway(PaymentGateway):
    def pay(self) -> None:
        print("Paying with Klarna")


class BitPayPaymentGateway(PaymentGateway):
    def pay(self) -> None:
        print("Paying with BitPay")


class PaymentProcessor:
    def __init__(self, payment_gateway: PaymentGateway) -> None:
        self.payment_gateway = payment_gateway

    def pay(self) -> None:
        self.payment_gateway.pay()


if __name__ == "__main__":
    payment_processor = PaymentProcessor(StripePaymentGateway())
    payment_processor.pay()

    payment_processor = PaymentProcessor(KlarnaPaymentGateway())
    payment_processor.pay()

    payment_processor = PaymentProcessor(BitPayPaymentGateway())
    payment_processor.pay()
```

In this example, we have a `PaymentProcessor` class that depends on an abstraction `PaymentGateway`. This means that we
can add as many payment gateways as we want without modifying the `PaymentProcessor` class itself.

## Conclusion

In this article, we have explored the SOLID principles and their implementation in Python. We have discussed how the
*SRP* can help in creating more organized and manageable classes, and how the *OCP* can make our code more extensible.
We have also examined the LSP to achieve more flexible code, the ISP for maintainable code, and even had a bit of fun
disarming civilians. Finally, we have explored how the *DIP* can increase code reusability.

That's all for today. See you next time!

## Further Reading

- Robert C. Martin - Clean Architecture: A Craftsman's Guide to Software Structure and Design.

