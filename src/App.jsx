import React from 'react'
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material'
import StudyBuddy from './StudyBuddy'


const theme = createTheme({

  const theme = createTheme({
    const theme = createTheme({
      const theme = createTheme({

        const theme = createTheme({const theme = createTheme({


const theme = createTheme({
  palette: {
    primary: {
      main: '#2196f3',
    },
    secondary: {
      main: '#f50057',
    },
    background: {
      default: '#f5f5f5',
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    h3: {
      fontWeight: 600,
    },
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
          borderRadius: 8,
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
        },
      },
    },
  },
})

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <div className="App">
        <StudyBuddy />
      </div>
    </ThemeProvider>
  )
}

export default App 
