import firebase from 'firebase/app';
import 'firebase/auth';

const firebaseConfig = {
    apiKey: "AIzaSyD4_q2k_7CvRXbP0MqGriFlFsucCxTL_CY",
    authDomain: "cybertools-1d68e.firebaseapp.com",
    projectId: "cybertools-1d68e",
    storageBucket: "cybertools-1d68e.firebasestorage.app",
    appId: "1:745494926973:web:6ebc1fed3e4b916de88314",
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
