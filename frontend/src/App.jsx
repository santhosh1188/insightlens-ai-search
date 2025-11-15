import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Upload from "./Upload";
import Search from "./Search";

function App() {
  return (
    <BrowserRouter>
      <nav className="p-4 bg-gray-100 shadow flex gap-4">
        <Link to="/" className="font-semibold">Search</Link>
        <Link to="/upload" className="font-semibold">Upload</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Search />} />
        <Route path="/upload" element={<Upload />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
