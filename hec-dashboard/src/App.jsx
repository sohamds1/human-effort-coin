import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

const API_URL = "http://127.0.0.1:8000"

function App() {
  const [stats, setStats] = useState({ total_users: 0, total_minted: 0, total_tasks: 0 })
  const [feed, setFeed] = useState([])
  const [loading, setLoading] = useState(true)
  const [simulationActive, setSimulationActive] = useState(true)
  const [selectedTransaction, setSelectedTransaction] = useState(null)

  const fetchData = async () => {
    try {
      const statsRes = await axios.get(`${API_URL}/stats`)
      const feedRes = await axios.get(`${API_URL}/feed?limit=20`)
      const statusRes = await axios.get(`${API_URL}/simulation/status`)
      setStats(statsRes.data)
      setFeed(feedRes.data)
      setSimulationActive(statusRes.data.active)
      setLoading(false)
    } catch (error) {
      console.error("Error fetching data:", error)
    }
  }

  const toggleSimulation = async () => {
    try {
      if (simulationActive) {
        await axios.post(`${API_URL}/simulation/stop`)
      } else {
        await axios.post(`${API_URL}/simulation/start`)
      }
      fetchData()
    } catch (error) {
      console.error("Error toggling simulation:", error)
    }
  }

  useEffect(() => {
    fetchData()
    const interval = setInterval(fetchData, 2000)
    return () => clearInterval(interval)
  }, [])

  const getVerdictIcon = (verdict) => {
    if (verdict === "APPROVED") return "✓"
    if (verdict === "REJECTED") return "✗"
    return "○"
  }

  const getTaskIcon = (type) => {
    if (type === "GARDENING") return "🌱"
    if (type === "CODING") return "💻"
    if (type === "CONSTRUCTION") return "🏗️"
    return "�"
  }

  return (
    <>
      <div className="dashboard-container">
        <header className="header-premium">
          <div className="header-left">
            <div className="logo-section">
              <div className="logo-icon">⚡</div>
              <div>
                <h1 className="title-premium">HEC Overseer</h1>
                <p className="subtitle">Proof-of-Labor Economic Oracle</p>
              </div>
            </div>
          </div>
          <div className="header-controls">
            <div className={`status-indicator ${simulationActive ? 'active' : 'paused'}`}>
              <div className="status-dot"></div>
              <span>{simulationActive ? 'System Active' : 'System Paused'}</span>
            </div>
            <button onClick={toggleSimulation} className="btn-control">
              {simulationActive ? '⏸ Pause' : '▶ Resume'}
            </button>
          </div>
        </header>

        <div className="stats-container">
          <div className="stat-card-premium">
            <div className="stat-icon">👥</div>
            <div className="stat-content">
              <div className="stat-label">Active Citizens</div>
              <div className="stat-value">{stats.total_users.toLocaleString()}</div>
              <div className="stat-trend">+{Math.floor(stats.total_users * 0.08)} this session</div>
            </div>
          </div>

          <div className="stat-card-premium highlight">
            <div className="stat-icon">💰</div>
            <div className="stat-content">
              <div className="stat-label">Global GDP</div>
              <div className="stat-value">{stats.total_minted.toFixed(1)} <span className="currency">EC</span></div>
              <div className="stat-trend">≈ ${(stats.total_minted * 25).toFixed(0)} USD @ $25/EC</div>
            </div>
          </div>

          <div className="stat-card-premium">
            <div className="stat-icon">📊</div>
            <div className="stat-content">
              <div className="stat-label">Verified Tasks</div>
              <div className="stat-value">{stats.total_tasks.toLocaleString()}</div>
              <div className="stat-trend">{stats.total_tasks > 0 ? Math.round((stats.total_minted / stats.total_tasks) * 10) / 10 : 0} EC/task avg</div>
            </div>
          </div>
        </div>

        <div className="feed-section-premium">
          <div className="section-header">
            <h2>Live Verification Stream</h2>
            <div className="feed-count">{feed.length} recent</div>
          </div>

          <div className="transactions-grid">
            {feed.map((item) => (
              <div
                key={item.id}
                className={`transaction-card ${item.verdict.toLowerCase()}`}
                onClick={() => setSelectedTransaction(item)}
              >
                <div className="transaction-header">
                  <div className="transaction-icon">{getTaskIcon(item.type)}</div>
                  <div className="transaction-meta">
                    <div className="transaction-type">{item.type}</div>
                    <div className="transaction-time">
                      {new Date(item.time).toLocaleTimeString()}
                    </div>
                  </div>
                  <div className={`verdict-pill ${item.verdict.toLowerCase()}`}>
                    <span className="verdict-icon">{getVerdictIcon(item.verdict)}</span>
                    {item.verdict}
                  </div>
                </div>
                <div className="transaction-body">
                  <div className="transaction-detail">
                    <span className="detail-label">Worker</span>
                    <span className="detail-value mono">{item.worker}</span>
                  </div>
                  <div className="transaction-detail">
                    <span className="detail-label">Duration</span>
                    <span className="detail-value">{item.hours} hours</span>
                  </div>
                </div>
                <div className="transaction-footer">
                  <span className="view-details">View full analysis →</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {selectedTransaction && (
        <div className="modal-overlay" onClick={() => setSelectedTransaction(null)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={() => setSelectedTransaction(null)}>×</button>

            <div className="modal-header">
              <div className="modal-icon-large">{getTaskIcon(selectedTransaction.type)}</div>
              <div>
                <h2>{selectedTransaction.type} Task</h2>
                <p className="modal-subtitle">Transaction Analysis</p>
              </div>
            </div>

            <div className="modal-sections">
              <div className="modal-section">
                <h3>📋 Task Details</h3>
                <div className="detail-grid">
                  <div className="detail-item">
                    <span className="label">Task ID</span>
                    <span className="value mono small">{selectedTransaction.id}</span>
                  </div>
                  <div className="detail-item">
                    <span className="label">Worker ID</span>
                    <span className="value mono small">{selectedTransaction.worker}</span>
                  </div>
                  <div className="detail-item">
                    <span className="label">Duration</span>
                    <span className="value">{selectedTransaction.hours} hours</span>
                  </div>
                  <div className="detail-item">
                    <span className="label">Submitted</span>
                    <span className="value">{new Date(selectedTransaction.time).toLocaleString()}</span>
                  </div>
                </div>
              </div>

              <div className="modal-section">
                <h3>🤖 Agent Verification</h3>
                <div className={`verification-result ${selectedTransaction.verdict.toLowerCase()}`}>
                  <div className="result-icon">{getVerdictIcon(selectedTransaction.verdict)}</div>
                  <div className="result-text">
                    <div className="result-verdict">{selectedTransaction.verdict}</div>
                    <div className="result-reason">
                      {selectedTransaction.verdict === "APPROVED"
                        ? "All verification checks passed. Metadata aligned with proof media. No fraud detected."
                        : "Visual evidence score below threshold. Insufficient proof of labor detected."}
                    </div>
                  </div>
                </div>
              </div>

              <div className="modal-section">
                <h3>💎 Economic Impact</h3>
                <div className="impact-grid">
                  <div className="impact-item">
                    <div className="impact-label">Tokens Minted</div>
                    <div className="impact-value">
                      {selectedTransaction.verdict === "APPROVED"
                        ? `${selectedTransaction.hours} EC`
                        : "0 EC"}
                    </div>
                  </div>
                  <div className="impact-item">
                    <div className="impact-label">USD Equivalent</div>
                    <div className="impact-value">
                      {selectedTransaction.verdict === "APPROVED"
                        ? `$${(selectedTransaction.hours * 25).toFixed(2)}`
                        : "$0.00"}
                    </div>
                  </div>
                  <div className="impact-item">
                    <div className="impact-label">Skill Multiplier</div>
                    <div className="impact-value">
                      {selectedTransaction.type === "CONSTRUCTION" ? "1.5x" :
                        selectedTransaction.type === "CODING" ? "1.2x" : "1.0x"}
                    </div>
                  </div>
                  <div className="impact-item">
                    <div className="impact-label">Transaction Fee</div>
                    <div className="impact-value">2% burned</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  )
}

export default App
