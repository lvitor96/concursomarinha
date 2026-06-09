import { auth, db } from './firebase.js';
import {
  GoogleAuthProvider,
  signInWithPopup,
  signOut,
  onAuthStateChanged,
} from 'firebase/auth';
import { doc, setDoc, getDoc, serverTimestamp } from 'firebase/firestore';

const provider = new GoogleAuthProvider();
provider.setCustomParameters({ prompt: 'select_account' });

/**
 * Inicia o observer de autenticação.
 * @param {(usuario: object|null) => void} callback
 */
function iniciarAuth(callback) {
  onAuthStateChanged(auth, async (usuario) => {
    if (usuario) {
      await garantirPerfil(usuario);
      callback(usuario);
    } else {
      callback(null);
    }
  });
}

/**
 * Abre o popup de login com Google.
 * @returns {Promise<object>} usuário autenticado
 */
async function fazerLogin() {
  try {
    const resultado = await signInWithPopup(auth, provider);
    return resultado.user;
  } catch (erro) {
    if (erro.code === 'auth/popup-closed-by-user') return null;
    throw erro;
  }
}

/**
 * Faz logout do usuário atual.
 */
async function fazerLogout() {
  await signOut(auth);
}

/**
 * Garante que o perfil do usuário existe no Firestore.
 * Cria apenas se não existir (primeira vez).
 */
async function garantirPerfil(usuario) {
  const ref = doc(db, 'users', usuario.uid, 'perfil', 'dados');
  const snap = await getDoc(ref);

  if (!snap.exists()) {
    await setDoc(ref, {
      nome: usuario.displayName,
      email: usuario.email,
      fotoURL: usuario.photoURL,
      dataCriacao: serverTimestamp(),
    });
  }
}

/**
 * Retorna o usuário autenticado atual ou null.
 */
function obterUsuario() {
  return auth.currentUser;
}

export { iniciarAuth, fazerLogin, fazerLogout, obterUsuario };
