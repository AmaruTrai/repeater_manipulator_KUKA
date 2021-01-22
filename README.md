# repeater_manipulator_KUKA
<p> Данное программный код реализует управление виртуальной моделью манипулятора KUKA в среде V-rep.</p>
<p> Алгоритм работы программы после инциализации следующий:</p>
<ol>
  <li>Программа получает данный от робота KUKA c помощью протокола UDP.</li>
  <li>Происходит распаковка полученный пакетов данных и получение угловых координат манипулятора.</li>
  <li>Полученные значения передаются в среду V-rep в которой виртуальная модель манипулятора отрабатывает движение релаьного робота.</li>
</ol>
<b>
<p> This program code implements control of the virtual model of the KUKA manipulator in the V-rep environment. </p>
<p> The algorithm of the program after initialization is as follows: </p>
<ol>
   <li> The program receives data from the KUKA robot using the UDP protocol. </li>
   <li> The received data packets are unpacked and the angular coordinates of the manipulator are obtained. </li>
   <li> The obtained values are transferred to the V-rep environment in which the virtual model of the manipulator works out the movement of the real robot. </li>
</ol>
