import 'package:flutter/material.dart';
import 'package:frontend/views/authentication/register_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Jobber',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      // Utilise la page d'accueil comme écran par défaut
      home: RegisterScreen(), // Modifier ici pour rediriger vers RegisterScreen ou HomeView
    );
  }
}
