import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';

export function Home() {
    return (
      <View style={styles.container}>
        <Text style={styles.text}>IndexXXX</Text>
        <StatusBar style="auto" />
        <TouchableOpacity style={styles.button}>
          <Text style={styles.text}>Button Text</Text>
        </TouchableOpacity>
      </View>
    );
  }
  
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#141325',
      alignItems: 'center',
      justifyContent: 'center',
    },
    button: {
      backgroundColor: 'blue',
      padding: 10,
      marginTop: 20,
    },
    text: {
      color: 'white',
    },
});
