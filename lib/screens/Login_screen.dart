import 'package:flutter/material.dart';
import 'register_screen.dart'; // Importe a tela de cadastro
import 'dashboard_screen.dart'; // Importe a tela Dashboard

// NOTA: Para este código funcionar, certifique-se que:
// 1. O arquivo 'register_screen.dart' existe.
// 2. O arquivo 'dashboard_screen.dart' existe.
// 3. A classe RegisterScreen e DashboardScreen estão definidas nesses arquivos.

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  
  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  String? _errorMessage;

  void _login() {
    setState(() {
      // 1. Validação básica de campos vazios
      if (_emailController.text.isEmpty || _passwordController.text.isEmpty) {
        _errorMessage = 'Por favor, preencha todos os campos.';
        return; // Sai da função se houver erro de validação
      } 
      
      // 2. Limpa a mensagem de erro se a validação passar
      _errorMessage = null;

      // --- SIMULAÇÃO DE LOGIN BEM-SUCEDIDO ---
      print('Simulando Login com: ${_emailController.text}');

      // *** CÓDIGO CRUCIAL: Navegação para a Dashboard ***
      // Usamos pushReplacement para que o usuário não possa voltar para o Login
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => const DashboardScreen()),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    // Usamos o tema definido no main.dart para cores e estilos
    final primaryColor = Theme.of(context).primaryColor;

    return Scaffold(
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 32),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Leve a Vida Leve',
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: primaryColor, 
                ),
              ),
              const SizedBox(height: 24),
              TextField(
                controller: _emailController,
                keyboardType: TextInputType.emailAddress,
                decoration: const InputDecoration(labelText: 'E-mail'),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _passwordController,
                obscureText: true,
                decoration: const InputDecoration(labelText: 'Senha'),
              ),
              const SizedBox(height: 16),
              if (_errorMessage != null)
                Padding(
                  padding: const EdgeInsets.only(bottom: 8.0),
                  child: Text(
                    _errorMessage!,
                    style: const TextStyle(color: Colors.red),
                  ),
                ),
              const SizedBox(height: 24),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: _login,
                  child: const Text('Entrar'),
                ),
              ),
              TextButton(
                onPressed: () {
                  // Navegação para a tela de cadastro
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => const RegisterScreen()),
                  );
                },
                child: const Text('Não tem conta? Cadastre-se'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}