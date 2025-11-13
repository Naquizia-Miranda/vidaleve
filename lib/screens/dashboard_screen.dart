import 'package:flutter/material.dart';
// Importe a tela de Perfil (futuramente usaremos)
// import '../views/perfil_view.dart';
import '../views/registro_diario_view.dart'; // Importe a tela de Registro Diário

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // Nesta View, idealmente usaríamos Provider/Consumer para buscar dados.

    return Scaffold(
      appBar: AppBar(
        title: const Text('Dashboard | Leve a Vida Leve'),
        backgroundColor: Theme.of(context).primaryColor, // Usando a cor do tema
        foregroundColor: Colors.white,
        actions: [
          IconButton(
            icon: const Icon(Icons.person),
            onPressed: () {
              // TODO: Implementar navegação para PerfilView (CRUD Usuario/Meta)
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Navegar para PerfilView (Em breve)'))
              );
            },
          ),
        ],
      ),
      // O corpo deve ser um resumo de estatísticas
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Card de Resumo do Peso (Exemplo)
            Card(
              color: Colors.white, 
              elevation: 4,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
              child: const ListTile(
                leading: Icon(Icons.scale, color: Color(0xFF00BCD4)),
                title: Text('Seu Progresso de Peso', style: TextStyle(fontWeight: FontWeight.bold)),
                subtitle: Text('Peso Atual: 75.2 kg | Meta: 70.0 kg'),
                trailing: Text('-5.0 kg', style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold)),
              ),
            ),
            const SizedBox(height: 16),

            const Text(
              'Metas de Hoje',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),

            // Cartões de Metas Diárias (Simulação)
            _buildGoalCard(
              title: 'Calorias Consumidas',
              value: '1200 / 1800 Kcal',
              icon: Icons.local_dining,
              progress: 0.66,
              color: const Color(0xFFFFCC80), // Laranja
            ),
            _buildGoalCard(
              title: 'Água Ingerida',
              value: '1.5 / 2.5 Litros',
              icon: Icons.water_drop,
              progress: 0.60,
              color: const Color(0xFF4FC3F7), // Azul
            ),
            _buildGoalCard(
              title: 'Atividade Física',
              value: '60 / 90 Minutos',
              icon: Icons.directions_run,
              progress: 0.66,
              color: const Color(0xFFA5D6A7), // Verde
            ),
          ],
        ),
      ),
      
      // Botão flutuante para adicionar novo registro (Ação principal)
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          // Implementação da navegação para a tela de RegistroDiarioView
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const RegistroDiarioView()),
          );
        },
        label: const Text('Novo Registro'),
        icon: const Icon(Icons.add),
        backgroundColor: const Color(0xFF4DD0E1), // Teal para destaque
        foregroundColor: Colors.white,
      ),
    );
  }

  // Widget auxiliar para os cartões de meta (Manter)
  Widget _buildGoalCard({
    required String title,
    required String value,
    required IconData icon,
    required double progress,
    required Color color,
  }) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8.0),
      child: Card(
        elevation: 2,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Icon(icon, color: color),
                  const SizedBox(width: 8),
                  Text(title, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w600)),
                ],
              ),
              const SizedBox(height: 8),
              Text(value, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
              const SizedBox(height: 8),
              // Barra de progresso linear (Manter)
              LinearProgressIndicator(
                value: progress,
                backgroundColor: color.withOpacity(0.3),
                valueColor: AlwaysStoppedAnimation<Color>(color),
              ),
            ],
          ),
        ),
      ),
    );
  }
}