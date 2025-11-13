import 'package:flutter/material.dart';
import 'screens/login_screen.dart';

void main() => runApp(LeveAVidaLeveApp());

class LeveAVidaLeveApp extends StatelessWidget {
  const LeveAVidaLeveApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Leve a Vida Leve',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: LoginScreen(),
    );
  }
}