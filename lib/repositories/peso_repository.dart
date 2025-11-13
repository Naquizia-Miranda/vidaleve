import 'package:cloud_firestore/cloud_firestore.dart';
import '../models/peso.dart';

// O repositório lida com a lógica de acesso aos dados (Firestore)
class PesoRepository {
  final FirebaseFirestore _firestore;
  
  // Nome da coleção no Firestore
  static const String _collectionName = 'registros_peso'; 

  PesoRepository(this._firestore);
  
  // Função para salvar ou atualizar um registro de peso
  Future<bool> salvarPeso(Peso peso) async {
    try {
      final collection = _firestore.collection(_collectionName);

      if (peso.id == null || peso.id == 0) {
        // Criar novo registro
        await collection.add(peso.toMap());
      } else {
        // Atualizar registro existente
        await collection.doc(peso.id.toString()).update(peso.toMap());
      }
      return true;
    } catch (e) {
      print('Erro ao salvar peso: $e'); // logar erro
      return false;
    }
  }

  // Função para buscar todos os registros de peso de um usuário
  Future<List<Peso>> getPesos(int usuarioId) async {
    try {
      final snapshot = await _firestore
          .collection(_collectionName)
          .where('usuarioId', isEqualTo: usuarioId)
          .orderBy('dataRegistro', descending: true) // Ordenar por data
          .get();

      // Mapeia os documentos do Firestore para objetos Peso
      return snapshot.docs.map((doc) => Peso.fromFirestore(doc)).toList();
    } catch (e) {
      print('Erro ao buscar pesos: $e');
      return [];
    }
  }
  
  // Função para deletar um registro de peso
  Future<bool> deletarPeso(int pesoId) async {
    try {
      await _firestore.collection(_collectionName).doc(pesoId.toString()).delete();
      return true;
    } catch (e) {
      print('Erro ao deletar peso: $e');
      return false;
    }
  }
}

// Comentário Instrucional (REMOVER): Lembre-se de adicionar a inicialização do Firebase
// e de usar o Provider para injetar este Repositório no main.dart.