import React, { useState } from 'react';
import { 
  Container, 
  Box, 
  Typography, 
  Button, 
  TextField, 
  Paper,
  Grid,
  Card,
  CardContent,
  CardActions,
  Radio,
  RadioGroup,
  FormControlLabel,
  FormControl,
  FormLabel,
  Alert,
  CircularProgress
} from '@mui/material';

const StudyBuddy = () => {
  const [mode, setMode] = useState('quiz'); // 'quiz' or 'ai'
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [feedback, setFeedback] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [score, setScore] = useState(0);
  const [quizComplete, setQuizComplete] = useState(false);

  const complexityQuestions = [
    {
      question: "What is the time complexity of binary search?",
      options: ["O(n)", "O(log n)", "O(n²)", "O(1)"],
      correct: 1
    },
    {
      question: "Which sorting algorithm has the best average-case time complexity?",
      options: ["Bubble Sort", "Quick Sort", "Selection Sort", "Insertion Sort"],
      correct: 1
    },
    {
      question: "What is the space complexity of a recursive function with depth n?",
      options: ["O(1)", "O(n)", "O(n²)", "O(2ⁿ)"],
      correct: 1
    }
  ];

  const handleModeChange = (newMode) => {
    setMode(newMode);
    setQuestion('');
    setAnswer('');
    setFeedback('');
    setCurrentQuestion(null);
    setScore(0);
    setQuizComplete(false);
  };

  const handleQuestionSubmit = async () => {
    if (!question.trim()) return;
    
    setIsLoading(true);
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000));
      setFeedback("Here's a detailed explanation of computational complexity...");
    } catch (error) {
      setFeedback("Sorry, there was an error processing your question.");
    } finally {
      setIsLoading(false);
    }
  };

  const startQuiz = () => {
    setCurrentQuestion(0);
    setScore(0);
    setQuizComplete(false);
  };

  const handleAnswerSubmit = (selectedOption) => {
    if (currentQuestion === null) return;
    
    const isCorrect = selectedOption === complexityQuestions[currentQuestion].correct;
    if (isCorrect) setScore(score + 1);

    if (currentQuestion < complexityQuestions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      setQuizComplete(true);
    }
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          Study Buddy
        </Typography>
        
        <Grid container spacing={2} sx={{ mb: 4 }}>
          <Grid item xs={6}>
            <Button 
              fullWidth 
              variant={mode === 'quiz' ? 'contained' : 'outlined'}
              onClick={() => handleModeChange('quiz')}
            >
              Quiz Mode
            </Button>
          </Grid>
          <Grid item xs={6}>
            <Button 
              fullWidth 
              variant={mode === 'ai' ? 'contained' : 'outlined'}
              onClick={() => handleModeChange('ai')}
            >
              AI Helper
            </Button>
          </Grid>
        </Grid>

        {mode === 'ai' ? (
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Ask a Question
            </Typography>
            <TextField
              fullWidth
              multiline
              rows={4}
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Ask anything about computational complexity..."
              sx={{ mb: 2 }}
            />
            <Button 
              variant="contained" 
              onClick={handleQuestionSubmit}
              disabled={isLoading || !question.trim()}
            >
              {isLoading ? <CircularProgress size={24} /> : 'Get Answer'}
            </Button>
            {feedback && (
              <Alert severity="info" sx={{ mt: 2 }}>
                {feedback}
              </Alert>
            )}
          </Paper>
        ) : (
          <Paper sx={{ p: 3 }}>
            {currentQuestion === null ? (
              <>
                <Typography variant="h6" gutterBottom>
                  Test your knowledge of computational complexity
                </Typography>
                <Button 
                  variant="contained" 
                  onClick={startQuiz}
                  sx={{ mt: 2 }}
                >
                  Start Quiz
                </Button>
              </>
            ) : !quizComplete ? (
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    Question {currentQuestion + 1} of {complexityQuestions.length}
                  </Typography>
                  <Typography variant="body1" gutterBottom>
                    {complexityQuestions[currentQuestion].question}
                  </Typography>
                  <FormControl component="fieldset">
                    <RadioGroup
                      value={answer}
                      onChange={(e) => handleAnswerSubmit(parseInt(e.target.value))}
                    >
                      {complexityQuestions[currentQuestion].options.map((option, index) => (
                        <FormControlLabel
                          key={index}
                          value={index}
                          control={<Radio />}
                          label={option}
                        />
                      ))}
                    </RadioGroup>
                  </FormControl>
                </CardContent>
              </Card>
            ) : (
              <>
                <Typography variant="h6" gutterBottom>
                  Quiz Complete!
                </Typography>
                <Typography variant="body1" gutterBottom>
                  Your score: {score} out of {complexityQuestions.length}
                </Typography>
                <Button 
                  variant="contained" 
                  onClick={startQuiz}
                  sx={{ mt: 2 }}
                >
                  Try Again
                </Button>
              </>
            )}
          </Paper>
        )}
      </Box>
    </Container>
  );
};

export default StudyBuddy; 