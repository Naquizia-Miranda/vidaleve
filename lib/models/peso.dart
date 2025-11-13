import 'package:cloud_firestore/cloud_firestore.dart';

class Peso {
  final int? id; // ID do documento no Firestore
  final int usuarioId; // ID do usuário que registrou
  final double pesoKg; // Peso registrado em quilos
  final DateTime dataRegistro; // Data e hora do registro

  Peso({
    this.id,
    required this.usuarioId,
    required this.pesoKg,
    required this.dataRegistro,
  });

  // Converte um DocumentSnapshot do Firestore para o objeto Peso
  factory Peso.fromFirestore(DocumentSnapshot doc) {
    final data = doc.data() as Map<String, dynamic>;
    
    // Converte Timestamp para DateTime
    DateTime dataReg = (data['dataRegistro'] as Timestamp).toDate();

    return Peso(
      id: int.tryParse(doc.id) ?? 0, // Usando o ID do documento como ID local (se for inteiro)
      usuarioId: data['usuarioId'] as int,
      pesoKg: data['pesoKg'] as double,
      dataRegistro: dataReg,
    );
  }

  // Converte o objeto Peso para Map (pronto para ser salvo no Firestore)
  Map<String, dynamic> toMap() {
    return {
      'usuarioId': usuarioId,
      'pesoKg': pesoKg,
      'dataRegistro': Timestamp.fromDate(dataRegistro),
    };
  }
}