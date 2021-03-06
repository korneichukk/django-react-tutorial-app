import './App.css';
import Header from './components/Header';
import NotesListPage from './pages/NotesListPage';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import NotePage from './pages/NotePage';


function App() {
  return (
    <div className="App">
      <Header />

      <BrowserRouter>
        <Routes>
          <Route path="/" element={<NotesListPage />}></Route>
          <Route path="/note/:id" element={<NotePage />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
