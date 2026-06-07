import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import {
  initializeFirestore,
  persistentLocalCache,
  persistentMultipleTabManager,
} from 'firebase/firestore';
import { getStorage } from 'firebase/storage';

const firebaseConfig = {
  apiKey: 'AIzaSyCjQa9aYPqUlCjyHYSjEtWgx2F0jIADkCE',
  authDomain: 'sedf-estudos-37168.firebaseapp.com',
  projectId: 'sedf-estudos-37168',
  storageBucket: 'sedf-estudos-37168.firebasestorage.app',
  messagingSenderId: '280309010125',
  appId: '1:280309010125:web:5bfd12e9d1a0757fe0a384',
};

const app = initializeApp(firebaseConfig);

// Firestore com persistência offline multi-aba habilitada
const db = initializeFirestore(app, {
  localCache: persistentLocalCache({
    tabManager: persistentMultipleTabManager(),
  }),
});

const auth = getAuth(app);
const storage = getStorage(app);

export { app, db, auth, storage };
