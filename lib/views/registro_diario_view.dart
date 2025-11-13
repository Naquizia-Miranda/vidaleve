import 'package:flutter/material.dart';

// Esta View será a "casca" que contém os 4 CRUDS diários.
// Usaremos um DefaultTabController para organizar as seções.

class RegistroDiarioView extends StatelessWidget {
  const RegistroDiarioView({super.key});

  @override
  Widget build(BuildContext context) {
    // Lista de abas (tabs)
    const List<Tab> tabs = <Tab>[
      Tab(icon: Icon(Icons.food_bank), text: 'Alimentação'),
      Tab(icon: Icon(Icons.fitness_center), text: 'Exercícios'),
      Tab(icon: Icon(Icons.water_drop), text: 'Água'),
      Tab(icon: Icon(Icons.scale), text: 'Peso'),
    ];

    return DefaultTabController(
      length: tabs.length,
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Novo Registro Diário'),
          backgroundColor: Theme.of(context).primaryColor,
          foregroundColor: Colors.white,
          // Barra de abas (TabBar) na parte inferior do AppBar
          bottom: TabBar(
            tabs: tabs,
            indicatorColor: Colors.white,
            labelColor: Colors.white,
            unselectedLabelColor: Colors.white70,
          ),
        ),
        body: TabBarView(
          children: <Widget>[
            // 1. Alimentação (Futuro: CrudAlimentoView)
            _BuildTabPlaceholder(title: 'Registro de Alimentação (CRUD)', color: Colors.orange.shade100),
            
            // 2. Exercícios (Futuro: CrudExercicioView)
            _BuildTabPlaceholder(title: 'Registro de Exercícios (CRUD)', color: Colors.green.shade100),

            // 3. Água (Futuro: CrudAguaView)
            _BuildTabPlaceholder(title: 'Registro de Água (CRUD)', color: Colors.blue.shade100),
            
            // 4. Peso (Futuro: CrudPesoView)
            _BuildTabPlaceholder(title: 'Registro de Peso (CRUD)', color: Colors.pink.shade100),
          ],
        ),
      ),
    );
  }
}

// Widget simples para visualizar onde cada aba ficará
class _BuildTabPlaceholder extends StatelessWidget {
  final String title;
  final Color color;

  const _BuildTabPlaceholder({required this.title, required this.color});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: color,
      alignment: Alignment.center,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            title,
            style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.grey.shade800),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 8),
          const Text('Aqui será implementado o CRUD específico.', style: TextStyle(color: Colors.grey)),
        ],
      ),
    );
  }
}