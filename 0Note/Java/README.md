| ArrayList | LinkedList |
|---|---------|
| Underlying implementation uses an array which is a continuous memory | Underlying implementation uses nodes which are not continuous memory |
| Fast access but slow on modification (insert/delete) | Slow on access but fast on modification (insert/delete) |

---

| Override | Overload |
|---|---------|
| Happens during class inheritance | Happens in the same class |
| Same method signature, i.e. same name and method parameters | Method names are the same but with different method parameters |
| Method call is determined at runtime | Method call is determined at compile time |

---

| Abstract class | Interface |
|---|---------|
| Normally has a mixture of abstract and non-abstract methods. These methods can be public / protected / private | Normally has only abstract and public methods.  |
| Doesn’t support multiple inheritance | Support multiple inheritance |
| Allow final, static, and non-static variables | Only allow static and final variables |
|Can implement an interface | Can’t extends an abstract class |
